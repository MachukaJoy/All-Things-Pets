from . import db,login_manager
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash
from flask import current_app 
import os,secrets

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    secure_password = db.Column(db.String(255),nullable = False)
    
    

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
    pic_path=db.Column(db.String(255),unique = True,nullable = False)
    name=db.Column(db.String(255),nullable = False)
    age=db.Column(db.String(255),nullable = False)
    color =db.Column(db.String(255),nullable = False)


    def save_p(self):
        db.session.add(self)
        db.session.commit()

        
    def __repr__(self):
        return f'Postpet {self.post}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def upload_img(post_img):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(post_img.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, "static/photos", picture_filename
    )
    post_img.save(picture_path)
    return picture_filename