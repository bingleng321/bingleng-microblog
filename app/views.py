
from flask import render_template,flash,redirect
from app import app
from forms import LoginForm


@app.route('/')
@app.route('/index')
def index():

	#fake user object
	user = {'nickname':'ming'}

	posts = [
			{
				'author':{'nickname':'John'},
				'body':'Beautiful day in AnHui'
			},	
			{
				'author':{'nickname':'Bing'},
				'body':'The Avengers movie was so cool!'
			}
		]
	return render_template('index.html',title='Home',user=user,posts = posts)

@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	return render_template('login.html',title='Sigin In',form = form)

