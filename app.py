#!/usr/bin/env python

from flask import (Flask, Blueprint, request, render_template, flash, url_for,
                    redirect, session)
from forms.forms import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    form = SurveyForm(request.form, csrf_enabled=False)
    return render_template('survey.html', form=form)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

