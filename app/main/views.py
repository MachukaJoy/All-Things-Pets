
from flask import render_template, redirect, url_for, abort, request
from . import main
from flask_login import login_required, current_user
from ..models import User, Claim,Comment, Upvote, Downvote
from .forms import UpdateProfile, ClaimForm, CommentForm
from .. import db,photos