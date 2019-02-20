from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mohit'}
    posts = [
        {
            'author': {'username': 'Vidula'},
            'body': 'Beautiful day in San Diego!'
        },
        {
            'author': {'username': 'Bob'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)