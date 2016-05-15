from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms import Required

class NameForm():
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
