from flask import render_template, redirect, url_for, abort, request,flash
from . import main
from flask_login import login_required, current_user
from ..models import User,Postpet,upload_img
from .forms import AdoptionForm,RequestForm,PostForm
from .. import db



@main.route('/')
def index():
    title = 'Pet-it'
    return render_template('index.html',title=title)

@main.route('/found')
@login_required
def found():
    pets= Postpet.query.all()

    return render_template('found.html',pets=pets)



@main.route('/adoption',methods =['GET','POST'])
@login_required
def adopt():
    form = AdoptionForm()
    if form.validate_on_submit():
        flash('Your request has been received successfully')
        return redirect(url_for(main.index))

    return render_template('adopt.html',form = form)


@main.route('/request',methods=['GET','POST'])
def request():
    form = RequestForm()
    if form.validate_on_submit():
        flash('Your request has been received successfully')
        return redirect(url_for(main.index))
    return render_template('request.html',form = form)

@main.route('/post',methods=['GET','POST'])
@login_required
def post():
    dogie=PostForm()   
    if dogie.image.data:
        pet_photo=upload_img(dogie.image.data)
        name =dogie.name.data 
        age =dogie.age.data 
        color=dogie.color.data 

        pet = Postpet(
            pic_path=pet_photo,
            name=name ,
            age=age,
            color=color
        )
        pet.save_p()
        return redirect(url_for('.found'))


    return render_template('post.html',dogie=dogie)


@main.route('/pet/delete/<int:pet_id>')
@login_required
def delete(pet_id):
    pet= Postpet.query.filter_by(id=pet_id).first()
    db.session.delete(pet)
    db.session.commit()
    return redirect(url_for('main.found'))