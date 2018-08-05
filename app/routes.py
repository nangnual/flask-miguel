from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': "Meeeeyyy"
    }
    posts = [
        {
            'author': {'username': 'joni'},
            'body': 'its sunshine'
        },
        {
            'author': {'username': 'udin'},
            'body': 'the grass is green'
        }
    ]
    return render_template('index.html', user=user, posts= posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form, title='Login Dulu')
