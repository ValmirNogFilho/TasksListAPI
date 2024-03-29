from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os 

app = Flask(__name__)
app.app_context().push()
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
postgres_url = "postgresql"+ os.environ.get("POSTGRES_URL")[8:] #psycopg2 doesn't supports "postgres" at the beginning of the url
app.config["SQLALCHEMY_DATABASE_URI"] = postgres_url

db = SQLAlchemy(app)

rsc = {
    r'/*' : {
        'origins': 'https://tasks-list-one.vercel.app'
    }
}

CORS(app, supports_credentials=True, resources=rsc)

from src import routes