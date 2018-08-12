from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello World!</h1>'


@app.route('/menu')
def menu():
	return '<h1>menu</h1>'

@app.route('/org')
def org():
	return '<h1>org</h1>'
	
if __name__ == '__main__':
	app.run(debug=True)
