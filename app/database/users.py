from app.extensions import db
from flask_login import UserMixin


# Users table
class Users(db.Model, UserMixin):
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(40), primary_key=True, index=True)
    phone_number = db.Column(db.String(30), nullable=False) 
    alt_number = db.Column(db.String(30))
    password = db.Column(db.String(170), nullable=False)
    address = db.Column(db.String(170))
    role = db.Column(db.String(15))
    about = db.Column(db.String(200))
    profile_img = db.Column(db.String(70))
    is_verified = db.Column(db.Boolean)
    social_media = db.relationship("SocialMedia", back_populates="user", lazy=True)

    
    def get_id(self):
        """returns user id"""
        return self.email


    def __repr__(self) -> str:
        return f"Users(name={self.name}, email={self.email}, " \
               f"password={self.password})"


    def __str__(self):
        return f"(name: {self.name}, email: {self.email} " \
                f"role: {self.role}, phone_number: {self.phone_number} " \
                f"alt_number: {self.alt_number}, verified: {self.is_verified})"
                

# company clients table              
class Clients(db.Model):
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(40), primary_key=True, index=True)
    phone_number = db.Column(db.String(30), nullable=False)
    alt_number = db.Column(db.String(30))
    address = db.Column(db.String(170))
    branch = db.Column(db.String(40))
    next_of_kin = db.Column(db.String(50))
    documents = db.relationship("Documents", back_populates="client", lazy=True)
    
    def __repr__(self) -> str:
        return f"Clients(name: {self.first_name} {self.last_name}, " \
                f"email: {self.email}, phone_number: {self.phone_number}, " \
                f"branch: {self.branch})"
    
    def __str__(self):
        return f"(name: {self.first_name} {self.last_name}, " \
                f"email: {self.email}, phone_number: {self.phone_number}, " \
                f"branch: {self.branch})"
    
    def get_id(self):
        """returns client id"""
        return self.email
    

# User social media table
class SocialMedia(db.Model):
    email = db.Column(
                db.String(40),
                db.ForeignKey(
                    'users.email',
                    onupdate="CASCADE",
                    ondelete="SET NULL",
                ),
                primary_key=True,
                index=True,
            )
    facebook = db.Column(db.String(50))
    twitter = db.Column(db.String(50))
    linkedin = db.Column(db.String(50))
    instagram = db.Column(db.String(50))
    user = db.relationship("Users", back_populates="social_media")
    
    def __repr__(self) -> str:
        return f"(email: {self.email}, facebook: {self.facebook}, " \
                f"twitter: {self.twitter}, linkedin: {self.linkedin}, " \
                f"instagram: {self.instagram})"
    
    def __str__(self):
        return f"(email: {self.email}, facebook: {self.facebook}, " \
                f"twitter: {self.twitter}, linkedin: {self.linkedin}, " \
                f"instagram: {self.instagram})"