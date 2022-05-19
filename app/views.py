# from flask import Flask, redirect, render_template,url_for
# from .forms import RegistrationForm, LoginForm
# from post import app


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route("/register", methods=['GET','POST'])
# def register():
#     form =  RegistrationForm()
#     # if form.validate_on_submit():
#     #     flash('Your account has been created successfully','success')
#     #     return redirect(url_for('home'))
#     return render_template('register.html', title = "Register", form=form)

# @app.route("/login", methods=['GET','POST'])
# def login():
#     form =  LoginForm()
#     return render_template('login.html', title = "login", form=form)



