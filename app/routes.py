from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Feature Request'}
    return render_template('index.html',title='Feature Request', user=user)
