from flask import (
    Blueprint,
    current_app,
    jsonify,
    request,
    redirect,
    render_template,
    send_from_directory,
    url_for,
)
from flask_login import current_user, login_required
from app.database.users import Clients
from app.database.documents import Documents
from app.database.notifications import Notifications
from app.database import db_helpers
from datetime import datetime
import os, time, uuid


bp = Blueprint("documents", __name__)

DOCUMENTS_CATEGORY = (
    "contract of agreement",
    "deed of transfer",
    "payment receipt",
)

ALL_BRANCHES = (
    "ihama",
    "obakhavbaye",
    "ikeja",
    "ajah",
    "abeokuta",
    "asaba",
)
    

@bp.route("/all_documents", methods=["GET", "POST"])
@login_required
def fetch_all_docs():
    """Returns all documents in the database"""

    if request.method == "POST":
        # if current_user.role == "admin":
        #     doc_status = None
        # else:
        #     doc_status = [
        #         Documents.is_deleted == False,
        #         Documents.is_thrashed == False,
        #     ]
            
        search_data = dict(request.form)
        results = db_helpers.document_filter_query(
            Documents,
            search_data.get("query", None),
            search_data.get("doc_category", None),
            search_data.get("client_branch", None),
        )
        
        if current_user.role != "admin":
            results = [file for file in results if file.is_thrashed == False and file.is_deleted == False]
        
        return render_template(
            "files/documents.html",
            branches = ALL_BRANCHES,
            doc_category = DOCUMENTS_CATEGORY,
            all_documents = results,
            user = current_user,
        )
    
    # for get request
    all_docs = db_helpers.fetch_records(
        Documents,
        is_deleted=False,
        is_thrashed=False,
    )

    
    return render_template(
        "files/documents.html",
        branches = ALL_BRANCHES,
        doc_category = DOCUMENTS_CATEGORY,
        all_documents = all_docs,
        user = current_user,
    )
    '''
    if not all_docs:
        current_app.logger.warning("returning an empty dictionary")
        return jsonify({}), 404
    
    return jsonify(
        [
            {
                "docId": "BLL-" + str(round(time.time() * 2)),
                "clientName": "James Smith",
                "clientEmail": "james.smith@example.com",
                "docType": "Deed of Transfer",
                "originBranch": "BLL Ihm",
            },
            {
                "docId": "BLL-" + str(round(time.time() * 2)),
                "clientName": "Sarah Snow",
                "clientEmail": "sarah.snow@example.com",
                "docType": "Contract Of Agreement",
                "originBranch": "BLL Obk",
            },
            {
                "docId": "BLL-" + str(round(time.time() * 2)),
                "clientName": "James Newton",
                "clientEmail": "james.newton@example.com",
                "docType": "Deed of Transfer",
                "originBranch": "BLL Ikj",
            },
        ]
    )
    '''


@bp.route("/thrashed_documents")
@login_required
def fetch_thrashed_docs():
    """returns thrashed documents"""

    thrashed_docs = db_helpers.fetch_records(
        Documents,
        is_thrashed=True,
        is_deleted=False,
    )
    
    return render_template(
        "files/thrashed_documents.html",
        branches = ALL_BRANCHES,
        doc_category = DOCUMENTS_CATEGORY,
        thrashed_documents = thrashed_docs,
        user = current_user,
    )


@bp.route("/upload_documents", methods=["GET", "POST"])
@login_required
def upload_doc():
    if request.method == "POST":
        upload_file = request.files["formFile"]
        client_data = dict(request.form)

        if upload_file.mimetype not in current_app.config["ALLOWED_FILE_TYPES"]:
            return jsonify(
                message = "Only .pdf, .doc and .docx files are allowed",
                category = "warning",
            ), 400
            
        new_file_name = "{}.{}".format(
            str(uuid.uuid4()), 
            upload_file.filename.split(".")[-1],
        )
   
        file_id = "BLL-" + str(round(time.time()) * 2)
        document_object = {
            "file_id": file_id,
            "doc_id": str(uuid.uuid4()),
            "doc_category": client_data["docCategory"],
            "file_name": new_file_name,
            "client_id": client_data["clientEmail"],
            "uploaded_by": current_user.name,
            "upload_time": datetime.utcnow(),
        }
        
        file_id = db_helpers.save_record(Documents, **document_object)
        db_helpers.save_record(
            Notifications,
            message=f"Document uploaded by {current_user.name}",
            category="success",
            user_id=current_user.email,
            created_at=datetime.utcnow(),
        )
        
        registerd = db_helpers.fetch_record(Clients, record_id=client_data["clientEmail"])
        if not registerd:
            client_object = {
                "first_name": client_data["firstName"],
                "last_name": client_data["lastName"],
                "email": client_data["clientEmail"],
                "address": client_data["clientAddress"],
                "phone_number": client_data["phoneNumber"],
                "branch": client_data["clientBranch"],
            }
            
            db_helpers.save_record(Clients, **client_object)

        # run the the upload to s3 on the bg
        upload_file.save(
            os.path.join(current_app.config["UPLOAD_FILE_FOLDER"], new_file_name),
            buffer_size= 250 * 1024,
        )

        return jsonify(
            message="File upload successful",
            category="info",
            status="success",
        )

    return render_template(
        "files/uploads.html",
        user=current_user,
        branches = ALL_BRANCHES,
        doc_category = DOCUMENTS_CATEGORY,
    )


@bp.route("/download_documents/<file_name>")
@login_required
def download_document(file_name):
    
    return send_from_directory(
        current_app.config["UPLOAD_FILE_FOLDER"],
        file_name,
    )
    

@bp.route("/thrash_document/<file_id>")
@login_required
def thrash_document(file_id):
    """Updates document status to thrash in database"""

    
    db_helpers.update_record(
        Documents,
        file_id,
        is_thrashed=True,
        thrashed_time=datetime.utcnow(),
        thrashed_by=current_user.name,
    )
    
    db_helpers.save_record(
        Notifications,
        message=f"{current_user.name} thrashed a document",
        category="warning",
        user_id=current_user.email,
        created_at=datetime.utcnow(),
    )

    return redirect(url_for("documents.fetch_all_docs"))



@bp.route("/restore_thrash/<file_id>")
@login_required
def restore_thrashed_document(file_id):
    """Updates is_thrashed document status to false in database"""

    
    db_helpers.update_record(
        Documents,
        file_id,
        is_thrashed=False,
        is_restored=True,
        restored_by=current_user.name,
    )

    db_helpers.save_record(
        Notifications,
        message=f"{current_user.name} restored a document",
        category="info",
        user_id=current_user.email,
        created_at=datetime.utcnow(),
    )

    return redirect(url_for("documents.fetch_thrashed_docs"))


@bp.route("/delete_document/<file_id>", methods=["PATCH"])
@login_required
def delete_document(file_id):
    """Deletes a document from the database"""

    db_helpers.update_record(
        Documents,
        file_id,
        is_deleted=True,
        deleted_time=datetime.utcnow(),
        deleted_by=current_user.name,
    )

    db_helpers.save_record(
        Notifications,
        message=f"{current_user.name} deleted a document",
        category="danger",
        user_id=current_user.email,
        created_at=datetime.utcnow(),
    )
    
    db_helpers.save_record(
        Notifications,
        message=f"{current_user.name} deleted a document",
        category="danger",
        user_id=current_user.email,
        created_at=datetime.utcnow(),
    )
    
    return jsonify(
        message="Document deleted successfully",
        category="success",
    )