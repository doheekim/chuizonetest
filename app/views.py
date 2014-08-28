from flask import render_template, request, redirect, url_for, Flask, session
from app import app, db
# from app.forms import AcademyForm
# from app.models import Academy
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


@app.route('/academy/create')
def academy_create():
	return render_template('academy_create.html')


# @app.route('/map', methods=['GET', 'POST'])
# def map():
# 	s1 = searcher_1.form.get
# 	s2 = searcher_2.form.get
# 	if request.method == 'POST':
# 		contents = db.session.query(Academy).filter(Academy.legion == s1).all() and db.session.query(Academy).filter(Academy.Category ==s2).all()
# 		return render_template('mapnlist.html', contents=contents)
# 	return render_template('main.html')


# @app.route('/academy/create/', methods=['GET', 'POST'])
# def article_create():
# 	form = AcademyForm()
# 	if request.method == 'GET':
# 		return render_template('academy_create.html', form=form)

# 	elif request.method == 'POST':
# 		if form.validate_on_submit():
			
# 			academy = Academy(
# 				academy_name=form.academy_name.data,
# 				teacher_name=form.teacher_name.data,
# 				academy_introduce=form.academy_introduce.data,
# 				teacher_introduce=form.teacher_introduce.data,
# 				curriculum_introduce=form.curriculum_introduce.data,
# 				academy_address=form.academy_address.data,
# 				welcome_line=form.welcome_line.data,
# 				phone_number=form.phone_number.data,
# 				class_time=form.class_time.data,
# 				class_fee=form.class_fee.data,
# 				homepage=form.homepage.data
# 				)
			
# 			db.session.add(academy)
# 			db.session.commit()

# 			# flash(u'Post Upload Success.', 'success')
# 			return redirect(url_for('academy'))
# 		return render_template('academy_create.html', form=form)