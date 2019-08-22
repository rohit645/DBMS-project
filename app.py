
from flask import Flask, request, flash, session, url_for, render_template, g, redirect
import sqlite3 as sql
import models as dbhandler

DATABASE = 'database.db'
app = Flask(__name__)
app.secret_key = 'supersecret'

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def get_db():
    con = sql.connect("database.db")
    return con

@app.route('/', methods=["POST","GET"])
def main():
    print('In the main page')
    if request.method == "POST":
        if request.form['accesslevel'] == 'admin':
            return redirect(url_for("adminlogin"))
        elif request.form['accesslevel'] == 'student':
            return redirect(url_for("studentlogin"))

    return render_template('main.html');

@app.route('/studentlogin', methods=["POST","GET"])
def studentlogin():
    if request.method=="POST":
        print('inside post request')
        rollno=request.form['rollno']
        password=request.form['password']
        check = dbhandler.validate(rollno, password)
        if check:
            print('student login successfully!')
            return redirect(url_for("studentpage"))
        else :
            print('student login failed!')
            return redirect(url_for("studentlogin"))
    return render_template('studentlogin.html');

@app.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html');

@app.route('/studentsignup', methods=["POST", "GET"])
def studentsignup():
    if request.method == 'POST':
        rollno = request.form['rollno']
        email = request.form['email']
        password = request.form['password']
        is_already_present = dbhandler.check_duplicate_student(rollno)
        if is_already_present:
            print('User: {} already exits'.format(rollno))
            return redirect(url_for("signup"))
        dbhandler.insertstudent(rollno, email, password)
        print('user added successfully!')
        return redirect(url_for("studentlogin"))
    return render_template('studentsignup.html');

app.run(port="3000", debug=True);
