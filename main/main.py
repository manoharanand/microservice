# from flask import Flask
# from markupsafe import escape
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS


from dataclasses import dataclass
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
import requests

app = Flask(__name__)
#this config line is to connect with myqsl_db   uname:pass@host/table_name
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

@app.route('/')
def index():
    return "Hello from flask app"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')