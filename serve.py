# -*- encoding: utf-8 ---------------------------------------------------------

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from views import *
from models import *

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()
