from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class CafeForm(FlaskForm):
    name = StringField("Cafe Name", validators=[DataRequired()])
    location = StringField("Location URL", validators=[DataRequired(), URL()])
    open_time = StringField("Open Time", validators=[DataRequired()])
    close_time = StringField("Close Time", validators=[DataRequired()])
    coffee_rating = StringField("Coffee Rating", validators=[DataRequired()])
    wifi_rating = StringField("Wifi Rating", validators=[DataRequired()])
    power_rating = StringField("Power Rating", validators=[DataRequired()])
    submit = SubmitField("Submit")