#-*-coding:utf-8-*-

from flask import render_template, request, redirect, url_for, Flask, session, jsonify
from app import app, db
from app.forms import AcademyForm
from app.models import Academy
import sys
reload(sys)
sys.setdefaultencoding('UTF8')


@app.route('/')
@app.route('/main')
def academy():

    return render_template('main.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
	if request.method == 'GET':
		s1 = request.args.get('searcher_1')
		s2 = request.args.get('searcher_2')
		data = 'fail'
		if s1 == 'kng':
			position = '37.49796298370522, 127.02761094942744'
			local =  u'강남구'
			return render_template('mapnlist.html', location = '37.49796298370522, 127.02761094942744')
		elif s1 == u'강동구':
			data = {'success':True, 'position':'37.53589682068908, 127.13235618124992', 'local': u'강동구'}
			return render_template('mapnlist.html', location = jsonify(data))	
		elif s1 == u'종로구':
			data = {'success':True, 'position':'37.57042061397492, 126.99213459583619', 'local': u'종로구'}
			return render_template('mapnlist.html', location = jsonify(data))
		return render_template('mapnlist.html', location = data)
	return render_template('mapnlist.html', location = data)

@app.route('/academy')
def mapnlist():
	return render_template('academy.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
	form=AcademyForm()
	if request.method == 'GET':
		return render_template('create.html', form=form)
	elif request.method == 'POST':
		if form.validate_on_submit():
			academy = Academy(
				academy_name=form.academy_name.data,
				teacher_name=form.teacher_name.data,
				academy_introduce=form.academy_introduce.data,
				teacher_introduce=form.teacher_introduce.data,
				curriculum_introduce=form.curriculum_introduce.data,
				academy_address=form.academy_address.data,
				welcome_line=form.welcome_line.data,
				phone_number=form.phone_number.data,
				class_time=form.class_time.data,
				class_fee=form.class_fee.data,
				homepage=form.homepage.data,
				location=form.location.data,
				category=form.category.data
				)

			db.session.add(academy)
			db.session.commit()
			return redirect(url_for('mapnlist'))

	return render_template('create.html', form=form)
