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
import os, uuid


bp = Blueprint("documents", __name__)

@bp.route("/all_documents")
@login_required
def fetch_all_docs():
    return render_template("documents.html")


@bp.route("/upload_documents", methods=["GET", "POST"])
#@login_required
def upload_doc():
    if request.method == "POST":
        upload_file = request.files["formFile"]
        client_data = dict(request.form)

        '''
        file_meta = {
            "content_type": upload_file.content_type,
            "file_name": upload_file.filename,
            "mimetype": upload_file.mimetype,
        }
        '''
        # check mimeType and file_size
        if upload_file.mimetype not in current_app.config["ALLOWED_FILE_TYPES"]:
            return jsonify(
                message = "Only .pdf, .doc and .docx files are allowed",
                category = "warning",
            ), 400
        
        upload_file.save(
            os.path.join(current_app.config["UPLOAD_FOLDER"], secure_filename(upload_file.filename)),
            buffer_size= 250 * 1024
        ) 
        # temporary store in file system b4 upload to s3
        # save data to db and file id
        # run the saving to file_system to as bg

   
        current_app.logger.info(f"upload file: {upload_file}")
        current_app.logger.info(dir(upload_file))

        return jsonify(
            message="File upload successful",
            category="success",
        )

        #current_app.logger.info(f"form data: {form_data}")
    
    return render_template("uploads.html")


@bp.route("/download_documents")
@login_required
def download_document():
    return "<h2>Download Document</h2>"


@bp.route("/delete_documents")
@login_required
def delete_document():
    return "<h2>Delete Document</h2>"