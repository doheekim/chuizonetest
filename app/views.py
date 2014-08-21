from flask import render_template, request, redirect, url_for, Flask, session
from app import app
import sys
reload(sys)
sys.setdefaultencoding('UTF8')


@app.route('/')
@app.route('/main')
def academy():

    return render_template('main.html')


@app.route('/mapnlist')
def main():

    return render_template('mapnlist.html')


@app.route('/academy')
def mapnlist():
	return render_template('academy.html')	