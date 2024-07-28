from app.extensions import db
from sqlalchemy.orm import relationship


class Documents(db.Model):
    file_id  = db.Column(db.String(35), primary_key=True, index=True)
    doc_id = db.Column(db.String(45), nullable=True, index=True, unique=True)
    doc_category = db.Column(db.String(30))
    file_name = db.Column(db.String(70))
    client_id = db.Column(
        db.String(35),
        db.ForeignKey(
            'clients.email',
            onupdate="CASCADE",
            ondelete="SET NULL",
        ), index=True)
    size = db.Column(db.Float)
    upload_time = db.Column(db.DateTime)
    uploaded_by = db.Column(db.String(50))
    file_url = db.Column(db.String(100))
    is_thrashed = db.Column(db.Boolean, default=False)
    thrashed_by = db.Column(db.String(50))
    thrashed_time = db.Column(db.DateTime)
    is_deleted = db.Column(db.Boolean, default=False)
    deleted_by = db.Column(db.String(50))
    deleted_time = db.Column(db.DateTime)
    is_restored = db.Column(db.Boolean, default=False)
    restored_by = db.Column(db.String(50))
    client = relationship("Clients", back_populates="documents")

    
    def __str__(self):
        return f"(file_id: {self.file_id}, " \
            f"doc_id: {self.doc_id}, " \
            f"doc_category: {self.doc_category}, " \
            f"file_name: {self.file_name}, " \
            f"client_id: {self.client_id}, " \
            f"url: {self.file_url},)"