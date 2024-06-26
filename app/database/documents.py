from app.extensions import db


class Documents(db.Model):
    file_id  = db.Column(db.String(15), primary_key=True, index=True)
    doc_id = db.Column(db.String(25), nullable=True)
    client = db.Column(db.String(50), nullable=False)
    size = db.Column(db.Float)
    upload_time = db.Column(db.DateTime)
    uploaded_by = db.Column(db.String(50))
    file_url = db.Column(db.String(100))
    
    def __str__(self):
        return {
            "doc_id": self.doc_id,
            "client": self.client,
            "url": self.file_url,
            "size": self.size
        }