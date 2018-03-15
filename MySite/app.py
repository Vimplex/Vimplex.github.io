from flask import Flask

from .Py.models import Apps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is secret!!'


from .Py.views import *
