from flask_pymongo import PyMongo
from MySite.app import app

app.config['MONGO_DBNAME'] = 'vimplex_db'
app.config['MONGO_URI'] = 'mongodb://Admin:global2020@ds255588.mlab.com:55588/vimplexs_users'

mongo = PyMongo(app)