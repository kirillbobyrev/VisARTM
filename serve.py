# -*- encoding: utf-8 ---------------------------------------------------------


from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


from views import *
from models import *


if __name__ == '__main__':
    app.run()
