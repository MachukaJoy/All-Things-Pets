# from flask_wtf import FlaskForm
# from wtforms import StringField, TextAreaField, SubmitField, SelectField
# from wtforms.validators import InputRequired

# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Update bio below..',validators = [InputRequired()])
#     submit = SubmitField('Save')

# class ClaimForm(FlaskForm):
#     title = StringField('Title', validators=[InputRequired()])
#     post = TextAreaField('Your Speech', validators=[InputRequired()])
#     location = StringField('Last spotted', validators=[InputRequired()])
#     submit = SubmitField('Claim')
    

# class CommentForm(FlaskForm):
#     comment = TextAreaField('Leave a comment',validators=[InputRequired()])
#     submit = SubmitField('Comment')

# class UpvoteForm(FlaskForm):
#     submit = SelectField('Like')



from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators  import InputRequired


class AdoptionForm(FlaskForm):
    type = StringField('Type of pet you wish to adopt',validators=[InputRequired()])
    gender = StringField('Gender of pet you wish to adopt',validators=[InputRequired()])
    pet = StringField('Do you own any pets?',validators=[InputRequired()])
    allergies = RadioField('Label',choices=[('yes','yes'),('no','no')],validators=[InputRequired()])
    veterinary = TextAreaField('Veterinary Credentials',validators=[InputRequired()])
    adopt = RadioField('Label',choices=[('adopt','adopt'),('claim','claim')],validators=[InputRequired()])
    submit =SubmitField('Submit')
    

class RequestForm(FlaskForm):
    type = StringField('Type of pet',validators=[InputRequired()])
    gender = StringField('Gender of pet',validators=[InputRequired()])
    breed = StringField('Breed of the pet',validators=[InputRequired()])
    location = StringField('Area where pet was Found/Lost',validators=[InputRequired()])
    aob = TextAreaField('Any additional information',validators=[InputRequired()])
    submit = SubmitField('Submit')

