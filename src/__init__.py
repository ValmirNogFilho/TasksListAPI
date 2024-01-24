from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.app_context().push()
app.config["SECRET_KEY"] = "1fbc7cd09f3e7b4d3f9c6eed"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)
CORS(app, supports_credentials=True)

from src import routes