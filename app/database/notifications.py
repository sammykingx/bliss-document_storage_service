from app.extensions import db


class Notifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(200))
    category = db.Column(db.String(20))
    user_id = db.Column(
        db.String(40),
        db.ForeignKey(
            'users.email',
            onupdate="CASCADE",
            ondelete="SET NULL",
        ), index=True)
    created_at = db.Column(db.DateTime)
    # user = db.relationship("Users", back_populates="notifications")

    
    def __repr__(self) -> str:
        return f"Notifications(message: {self.message}, " \
            f"category: {self.category}, " \
            f"user_id: {self.user_id}, " \
            f"created_at: {self.created_at}"
    
    def __str__(self):
        return f"(message: {self.message}, " \
            f"category: {self.category}, " \
            f"user_id: {self.user_id}, " \
            f"created_at: {self.created_at}"

    def get_id(self):
        """returns notification id"""
        return self.id