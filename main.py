import sqlite3

import flask
from flask import Flask, render_template, url_for, request, redirect, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlbase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Qwerty123'
app.config['SECURITY_PASSWORD_SALT'] = 'mEd6CQHzXS6buJFbGKu9Cfm4g'
app.config['SECURITY_PASSWORD_HASH'] = 'sha512_crypt'
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy(app)








@app.route('/')
@app.route('/main')
def main():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')