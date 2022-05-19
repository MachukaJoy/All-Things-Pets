from . import db,login_manager
from datetime import datetime
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    secure_password = db.Column(db.String(255),nullable = False)
    profile_pic_path = db.Column(db.String())
    claims = db.relationship('Claim', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvote = db.relationship('Upvote',backref='user',lazy='dynamic')
    
    

    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password,password) 
    
    def save_u(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f'User {self.username}'

class Postpet(db.Model):
    __tablename__ = 'postpets'
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(255),nullable = False)
    gender = db.Column(db.String(255),nullable = False)
    breed = db.Column(db.String(255),nullable = False)
    location = db.Column(db.String(255),nullable = False)
    aob = db.Column(db.Text(), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def save_p(self):
        db.session.add(self)
        db.session.commit()

        
    def __repr__(self):
        return f'Postpet {self.post}'

class Claim(db.Model):
    __tablename__ = 'claims'
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(255),nullable = False)
    gender = db.Column(db.String(255),nullable = False)
    pet = db.Column(db.String(255),nullable = False)
    allergies = db.Column(db.String(255),nullable = False)
    veterinary = db.Column(db.String(255),nullable = False)
    adopt = db.Column(db.String(255),nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def save_p(self):
        db.session.add(self)
        db.session.commit()

        
    def __repr__(self):
        return f'Claim {self.post}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)