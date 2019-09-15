from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap


app = Flask(__name__)


# Setting up configuration
app.config.from_object(DevConfig)
# Initializing Flask Extensions
bootstrap = Bootstrap(app)


from .main import views
