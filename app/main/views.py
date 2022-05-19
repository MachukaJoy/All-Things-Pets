# from flask import render_template, redirect, url_for, abort, request
# from . import main
# from flask_login import login_required, current_user
# from ..models import User, Claim,Comment, Upvote, Downvote
# from .forms import UpdateProfile, ClaimForm, CommentForm
#from .. import db,photos


from flask import Flask,render_template,redirect,url_for
from .forms import AdoptionForm,RequestForm
from ..models import User
from . import main
from .. import db




@main.route('/')
def index():
    title = 'Pet-it'
    return render_template('index.html',title=title)

@main.route('/found')
def found():
     return render_template('found.html')



@main.route('/adoption',methods =['GET','POST'])
def adopt():
    form = AdoptionForm()
    if form.validate_on_submit():
        type = form.type.data
        gender = form.gender.data
        pet = form.pet.data
        allergies = form.pet.data
        veterinary = form.veterinary.data
        adopt = form.adopt.data 
        new_adopt = User(type,gender,pet,allergies,veterinary,adopt)
        new_adopt.save_adopt()
        return redirect(url_for('/'))

    return render_template('adopt.html',form = form)


@main.route('/request',methods=['GET','POST'])
def request():
    form = RequestForm()
    if form.validate_on_submit():
        type = form.type.data
        gender = form.gender.data
        breed = form.breed.data
        location = form.location
        aob = form.aob.location
        new_request = User(type,gender,breed,location,aob)
        new_request.save_request()
    return render_template('request.html',form = form)



