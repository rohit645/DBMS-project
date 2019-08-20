from flask import Flask, request
from flask import render_template
from flask import g
import sqlite3 
import models as dbhandler

DATABASE = 'database.db'
app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def main():
    # return 'hi there!';
    # cur = get_db().cursor()
    return render_template('main.html');

@app.route('/login')
def login():
    return render_template('login.html');

@app.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html');

@app.route('/signup', methods=["POST", "GET"])
def signup():
    print(request)
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        dbhandler.insertuser(email, username, password)
    return render_template('login.html');

app.run(port="3000", debug=True);
