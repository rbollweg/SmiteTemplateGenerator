__author__ = 'The Gibs'

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from smiteapp import views