#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Raccoon, Trashcan, Visit

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def index():
    return "Hello world"

# write your routes here!

@app.delete('/raccoons/<int:id>')
def delete_raccoon_by_id (id):
    try:
        raccoon = Raccoon.query.filter(Raccoon.id == id).first()
        db.session.delete(raccoon)
        db.commit()
        return {}, 204
    except:
        return ({'error: raccoon not found'}), 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)