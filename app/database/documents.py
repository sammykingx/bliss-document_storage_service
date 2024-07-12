from app.extensions import db


class Documents(db.Model):
    file_id  = db.Column(db.String(35), primary_key=True, index=True)
    doc_id = db.Column(db.String(45), nullable=True, index=True, unique=True)
    doc_category = db.Column(db.String(30))
    file_name = db.Column(db.String(70))
    client_id = db.Column(db.String(35), index=True)
    client_branch = db.Column(db.String(40))
    size = db.Column(db.Float)
    upload_time = db.Column(db.DateTime)
    uploaded_by = db.Column(db.String(50))
    file_url = db.Column(db.String(100))
    
    def __str__(self):
        return {
            "doc_id": self.doc_id,
            "doc_category": self.doc_category,
            "file_name": self.file_name,
            "client_id": self.client_id,
            "client_branch": self.client_branch,
            "url": self.file_url,
        }