from flask import render_template
from app import app

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
