
from flask import render_template, redirect, url_for, abort, request
from . import main
from flask_login import login_required, current_user
from ..models import User, Claim,Comment, Upvote, Downvote
from .forms import UpdateProfile, ClaimForm, CommentForm
from .. import db,photos
from app import main

@main.route('/')
def index():
    title = 'Pet-it'
    return render_template('index.html',title=title)



@main.route('/found')
def found():
    return render_template('found.html')
