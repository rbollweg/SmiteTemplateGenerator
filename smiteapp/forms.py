__author__ = 'The Gibs'

from flask.ext.wtf import Form
from wtforms.fields.html5 import DateTimeField
from wtforms_components import TimeField, StringField, SelectField
from wtforms.fields import TextAreaField
from wtforms.validators import DataRequired
from smiteapp import parser


class SearchForm(Form):
    matchID = StringField('matchID', validators=[DataRequired()])
    game_name = StringField('game_name', default="game1")
    team1 = StringField('team1')
    team2 = StringField('team2')
    blue_towers = StringField('blue_towers')
    blue_phoenixes = StringField('blue_phoenixes')
    red_towers = StringField('red_towers')
    red_phoenixes = StringField('red_phoenixes')
    red_score = StringField('red_score')
    blue_score = StringField('blue_score')
    tournament_name = StringField('tournament_name')
    daylight_savings_time = SelectField('DST',
                                        choices=[("no", 'No'), ("yes", 'Yes'), ("spring", 'Spring'), ("fall", 'Fall')])



