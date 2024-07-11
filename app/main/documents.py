from flask import (
    Blueprint,
    current_app,
    jsonify,
    request,
    render_template,
    send_from_directory,
)
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from app.database.documents import Documents
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

@bp.route("/render_documents")
@login_required
def render_page():
    return render_template("documents.html")
    

@bp.route("/all_documents", methods=["GET", "POST"])
@login_required
def fetch_all_docs():
    if request.method == "POST":
        search_data = dict(request.form)
        current_app.logger.info(f"search data: {search_data}")
        results = db_helpers.document_filter_query(
            Documents,
            search_data["search_input"],
            search_data["doc_category"],
            search_data["client_branch"],
        )
        
        for res in results:
            current_app.logger.info(f"result name: {res.file_name}")
        
        return render_template(
            "documents.html",
            branches = ALL_BRANCHES,
            doc_category = DOCUMENTS_CATEGORY,
            all_documents = results,
        )
        
    all_docs = db_helpers.fetch_records(Documents)

    return render_template(
        "documents.html",
        branches = ALL_BRANCHES,
        doc_category = DOCUMENTS_CATEGORY,
        all_documents = all_docs,
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


@bp.route("/upload_documents", methods=["GET", "POST"])
@login_required
def upload_doc():
    if request.method == "POST":
        upload_file = request.files["formFile"]
        client_data = dict(request.form)

        # check mimeType and file_size
        if upload_file.mimetype not in current_app.config["ALLOWED_FILE_TYPES"]:
            return jsonify(
                message = "Only .pdf, .doc and .docx files are allowed",
                category = "warning",
            ), 400
            
        new_file_name = "{}.{}".format(
            str(uuid.uuid4()), 
            upload_file.filename.split(".")[-1],
        )

        upload_file.save(
            os.path.join(current_app.config["UPLOAD_FOLDER"], new_file_name),
            buffer_size= 250 * 1024,
        )
        
        file_id = "BLL-" + str(round(time.time()) * 2)
        record_object = {
            "file_id": file_id,
            "doc_id": str(uuid.uuid4()),
            "doc_category": client_data["clientBranch"],
            "file_name": new_file_name, #secure_filename(upload_file.filename),
            "client_id": client_data["clientEmail"],
            "uploaded_by": current_user.name,
            "upload_time": datetime.utcnow(),
        }
        
        file_id = db_helpers.save_record(Documents, **record_object)
        # temporary store in file system b4 upload to s3
        # save data to db and file id
        # run the saving to file_system to as bg

        current_app.logger.info(upload_file.filename, new_file_name)

        return jsonify(
            message="File upload successful",
            category="success",
        )

    return render_template(
        "uploads.html",
        branches = ALL_BRANCHES,
        doc_category = DOCUMENTS_CATEGORY,
    )


@bp.route("/download_documents/<file_name>")
@login_required
def download_document(file_name):
    
    return send_from_directory(
        current_app.config["UPLOAD_FOLDER"],
        file_name,
    )
    
    # return "<h2>Download Document</h2>"


@bp.route("/delete_documents")
@login_required
def delete_document():
    return "<h2>Delete Document</h2>"