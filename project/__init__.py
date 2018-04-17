# -*- coding: utf-8 -*-

__version__ = '0.1'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('project.settings')

db = SQLAlchemy(app)

import models
import controller


