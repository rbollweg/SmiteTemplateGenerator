__author__ = 'The Gibs'

import urllib.request

from flask import render_template, flash

from smiteapp import app, parser
from smiteapp.forms import SearchForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        flash("Parse requested for %s" % form.matchID)
        matchID = form.matchID._value()
        team1 = form.team1._value()
        team2 = form.team2._value()
        tournament_name = form.tournament_name._value()
        daylight_savings_time = form.daylight_savings_time.data
        game_name = form.game_name._value()
        blue_towers = form.blue_towers._value()
        blue_phoenixes = form.blue_phoenixes._value()
        red_towers = form.red_towers._value()
        red_phoenixes = form.red_phoenixes._value()
        red_score = form.red_score._value()
        blue_score = form.blue_score._value()
        template = parser.spider(matchID, game_name, team1, team2, red_score, blue_score, blue_towers, blue_phoenixes, red_towers, red_phoenixes, tournament_name, daylight_savings_time)
        return render_template("results.html",
                               title='Results',
                               template=template,
                               form=form)
    return render_template("index.html",
                           title='Home',
                           form=form)



