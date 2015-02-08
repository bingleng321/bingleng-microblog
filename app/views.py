
from flask import render_template
from app import app

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

