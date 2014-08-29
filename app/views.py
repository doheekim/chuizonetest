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
def main():
    return render_template('main.html')


@app.route('/mapnlist', methods=['GET', 'POST'])
def mapnlist():
	return render_template('mapnlist.html')


@app.route('/mapdata', methods=['GET', 'POST'])
def mapdata():
	if request.method == 'GET':
		s1 = request.args.get('searcher_1')
		s2 = request.args.get('searcher_2')
		data = {'success':True, 'gu_latlng': 'fail', 'gu_name': u'실패'}
		if s1 == 'kng':
			data = {'success':True, 'gu_latlng': '37.49796298370522, 127.02761094942744', 'gu_name': u'강남구'}
			return jsonify(data)
		elif s1 == 'kdg':
			data = {'success':True, 'gu_latlng': '37.53589682068908, 127.13235618124992', 'gu_name': u'강동구'}
			return jsonify(data)
		elif s1 == 'jrg':
			data = {'success':True, 'gu_latlng': '37.57042061397492, 126.99213459583619', 'gu_name': u'종로구'}			
			return jsonify(data)
		return jsonify(data)
	return jsonify(data)


@app.route('/academy')
def academy():
	return render_template('academy.html')


@app.route('/academy/create', methods=['GET', 'POST'])
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
				category=form.category.data,
				academy_latlng=form.academy_latlng.data
				)

			db.session.add(academy)
			db.session.commit()
			# Have to Make line 74, "id"
			return redirect(url_for('academy_detail', id=id))
		return render_template('create.html', form=form)
	return render_template('create.html', form=form)


@app.route('/academy/detail/<int:id>', methods=['GET'])
def academy_detail(id):
	academy = Academy.query.get(id)

	return render_template('academy_test.html', academy=academy)
