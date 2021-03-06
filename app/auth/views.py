from flask import redirect, render_template,url_for,request,flash
from .forms import RegistrationForm, LoginForm
from . import auth
from ..models import User 
from .. import db
from flask_login import login_user,logout_user,login_required

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "All_things_pets login"
    return render_template('auth/login.html',login_form = login_form,title=title)


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',registration_form = form) 

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been successfully logged out')
    return redirect(url_for("main.index"))