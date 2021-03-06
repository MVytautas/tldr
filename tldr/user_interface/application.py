from flask import Flask, render_template, url_for, request

app= Flask(__name__)

@app.route('/home')
def index():
	url_for('static', filename='css/bootstrap.min.css', _external=True)
	url_for('static', filename='css/home.css', _external=True)
	return render_template('index.html')

@app.route('/review', methods=['GET','POST'])
def review():
	url_for('static', filename='css/bootstrap.min.css', _external=True)
	url_for('static', filename='css/home.css', _external=True)
	url = request.args.get('url')
	## Here we should do the scrapping

	## Here we obtain the pros and cons

	## Harcoded sample
	name = "3D-Printer"
	calification = 4
	pros = ["BUENO", "bonito", "barato"]
	cons = ["malo", "malito", "caro"]

	return render_template('review.html', data = [name,calification,pros,cons])


@app.errorhandler(404)
def error(e):
	url_for('static', filename='css/404.css', _external=True)
	return render_template('404.html'), 404


if __name__ == '__main__':
	app.run(host='localhost')
