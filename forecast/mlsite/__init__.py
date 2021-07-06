import os
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'



from mlsite.core.views import core
from mlsite.predict.views import predict
from mlsite.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(predict)
app.register_blueprint(error_pages)
