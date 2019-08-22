from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('test', __name__)

@bp.route('/addques', methods=("POST", "GET"))
@login_required
def addques():
    if request.method == 'POST':
        ques = request.form['ques']
        optionA = request.form['optionA']
        optionB = request.form['optionB']
        optionC = request.form['optionC']
        optionD = request.form['optionD']
        ans = request.form['ans']
        error = None

        if not ques:
            error = 'question is required!'
        elif not optionA:
            error = 'optionA is required!'
        elif not optionB:
            error = 'optionB is required!'
        elif not optionC:
            error = 'optionC is required!'
        elif not optionD:
            error = 'optionD is required!'
        elif not ans:
            error = 'ans is required!'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO tests (ques, optionA, optionB, optionC, optionD, ans)'
                ' VALUES (?, ?, ?, ?, ?, ?)',
                (ques, optionA, optionB, optionC, optionD, ans)
            )
            db.commit()
            return redirect(url_for('index'))

    return render_template('test/addques.html')