#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('UTF8')

from flask import render_template, request, redirect, url_for, Flask, session, jsonify, make_response, request
from app import app, db
from app.forms import AcademyForm
from app.models import Academy
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import desc

@app.route('/')
@app.route('/main')
def main():
	return render_template('main.html')

@app.route('/map')
def map():
	return render_template('map.html')

@app.route('/mapnlist')
def mapnlist():
	return render_template('mapnlist.html')

@app.route('/mapdata')
def mapdata():
	# mapdata = Academy.query.filter(Academy.location == 'kng').first()
	location = str(request.args.get('searcher_1'))
	mapdata = db.session.query(Academy).filter(Academy.academy_latlng == "kng").order_by(desc(Academy.id))

	resp = {}
	resp["data"] = []
	temp = {}

	for academy in mapdata:
		temp['id'] = academy.id
		temp['name'] = academy.academy_name
		temp['latlang'] = academy.academy_latlng

		resp["data"].append(temp)
		temp = {}	

	return jsonify(resp)

@app.route('/academy')
def academy():
	return render_template('academy.html')


@app.route('/academy/create', methods=['GET', 'POST'])
def academy_create():
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
				academy_latlng=form.academy_latlng.data,
				image_1=form.image_1.data,
				image_2=form.image_2.data,
				image_3=form.image_3.data,
				image_4=form.image_4.data,
				image_5=form.image_5.data
				)

			db.session.add(academy)
			db.session.commit()

			return render_template('main.html')
		return render_template('create.html', form=form)
	return render_template('create.html', form=form)


@app.route('/academy/<int:id>', methods=['GET'])
def academy_detail(id):
	academy = Academy.query.get(id)

	return render_template('academy_test.html', academy=academy)


# @app.route('/academy/update/<int:id>', methods=['GET', 'POST'])
# def academy_update():
# 	academy = Academy.query.get(id)
# 	form = AcademyForm(request.form, obj=academy)

# 	if request.method == 'GET':
# 		return render_template('update.html', form=form)

# 	elif request.method == 'POST':
# 		if form.validate_on_submit():
# 			form.populate_obj(academy)
# 			db.session.commit()
# 			return redirect(url_for('academy_detail', id=id))
# 		return render_template('update.html', form=form)
