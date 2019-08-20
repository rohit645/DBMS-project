from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    # return 'hi there!';
    return render_template('main.html');

@app.route('/login')
def login():
    return render_template('login.html');

# @app.route('/adminlogin')
# def adminlogin():
#     return render_template('adminlogin.html');

# @app.route('/signup')
# def signup():
#     return render_template('signup.html');

# @app.route('/about')
# def about():
#     return 'The about page'

app.run(port="3000", debug=True);
