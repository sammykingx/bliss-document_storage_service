from app.extensions import db


class Users(db.Model):
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(40), primary_key=True, index=True)
    password = db.Column(db.String(170), nullable=False)
    role = db.Column(db.String(15))
    is_verified = db.Column(db.Boolean)

    
    def get_id(self):
        """returns user id"""
        return self.email


    def __repr__(self):
        return f"Users(name={self.name}, email{self.email}, " \
               f"password={self.password})"


    def __str__(self):
        return {
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "verified": self.is_verified,
        }