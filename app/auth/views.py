from flask import Flask, redirect, render_template,url_for
from .forms import RegistrationForm, LoginForm
from . import auth


@auth.route('/')
def index():
    return render_template('index.html')

@auth.route("/register", methods=['GET','POST'])
def register():
    form =  RegistrationForm()
    return render_template('auth/register.html', title = "Register", form=form)

@auth.route("/login", methods=['GET','POST'])
def login():
    form =  LoginForm()
    return render_template('auth/login.html', title = "login", form=form)



