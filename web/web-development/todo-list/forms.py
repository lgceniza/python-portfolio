from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
  task = StringField('Task Description', validators=[DataRequired()])
  submit = SubmitField('Add')

class UpdateTaskForm(FlaskForm):
  task = StringField('Task Description', validators=[DataRequired()])
  submit = SubmitField('Update')
