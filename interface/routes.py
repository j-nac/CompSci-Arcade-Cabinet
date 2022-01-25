from flask import render_template, url_for
from interface import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('home.html', title='Home')
