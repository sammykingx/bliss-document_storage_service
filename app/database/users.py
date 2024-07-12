from app.extensions import db
from flask_login import UserMixin


# Users table to represent the company staff
class Users(db.Model, UserMixin):
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(40), primary_key=True, index=True)
    password = db.Column(db.String(170), nullable=False)
    role = db.Column(db.String(15))
    is_verified = db.Column(db.Boolean)

    
    def get_id(self):
        """returns user id"""
        return self.email


    def __repr__(self) -> str:
        return f"(name={self.name}, email={self.email}, " \
               f"password={self.password})"


    def __str__(self):
        return f"(name: {self.name}, email: {self.email} " \
                f"role: {self.role} verified: {self.is_verified})"
                

# company clients table              
class Clients(db.Model):
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(40), primary_key=True, index=True)
    phone_number = db.Column(db.String(30), nullable=False)
    alt_number = db.Column(db.String(30))
    address = db.Column(db.String(170))
    next_of_kin = db.Column(db.String(50))
    
    def __repr__(self) -> str:
        return f"(name: {self.first_name} {self.last_name}) " \
                f"email: {self.email}, phone_number: {self.phone_number})"