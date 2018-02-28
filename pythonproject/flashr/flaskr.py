# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello World! test'
@app.route('/test/')
def test():
	return url_for('hello_world')
@app.route('/user/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')