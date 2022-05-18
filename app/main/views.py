from app import main
from flask import render_template


@main.route('/found')
def found():
    return render_template('found.html')