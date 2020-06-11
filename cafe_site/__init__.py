from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('cafe_site.config')

db = SQLAlchemy(app)

import cafe_site.views
