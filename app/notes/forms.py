from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class NoteForm(FlaskForm):
    title = StringField(
        'Title', validators=[DataRequired(), Length(max=200)]
    )
    body = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Save')
