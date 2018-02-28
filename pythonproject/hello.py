from flask import Flask, url_for
app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello World! test'
@app.route('/test/')
def test():
	return url_for('hello_world')
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
	return 'User %s' % username
if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')


