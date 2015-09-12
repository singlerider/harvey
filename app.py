#!/usr/bin/env python

from flask import (Flask, Blueprint, request, render_template, flash, url_for,
                    redirect, session)
from forms.forms import *
app = Flask(__name__)

app.secret_key = 'password'

def login_required(f):
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def hello_world():
    return render_template('index.html')

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    form = SurveyForm(request.form, csrf_enabled=False)
    return render_template('survey.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Incorrect username and/or password'
        else:
            session['logged_in'] = True
            return redirect(url_for('success'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return "Success!"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

