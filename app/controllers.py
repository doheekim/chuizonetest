from flask import render_template, request, redirect, url_for, Flask, session
# from werkzeug.security import generate_password_hash, check_password_hash
# from sqlalchemy import desc
from app import app
# from app import app, db
# from app.forms import AcademyForm
# from app.models import Article, Comment, User
import sys
reload(sys)
sys.setdefaultencoding('UTF8')


@app.route('/')
@app.route('/academy')
def academy():

    return render_template('academy.html')


@app.route('/main')
def main():

    return render_template('main.html')


# @app.route('/academy_create', methods=['GET', 'POST'])
# def academy_upload():
# 	form = AcademyForm()
# 	if request.method == 'GET':
# 		return render_template('academy_create.html', .........., ..........)

# 	elif request.method == 'POST':
# 		if form.validate_on_submit():

# 			academy = Academy(
# 				academy_name = form.academy_name.data,
# 				teacher_name = form.teacher_name.data,
# 				academy_introduce = form.academy_introduce.data,
# 				teacher_introduce = form.teacher_introduce.data,
# 				curriculum_introduce = form.curriculum_introduce.data,
# 				academy_address = form.academy_address.data,
# 				welcome_line = form.welcome_line.data,
# 				phone_number = form.phone_number.data,
# 				class_time = form.class_time.data,
# 				class_fee = form.class_fee.data,
# 				homepage = form.homepage.data
# 				)

# 			db.session.add(academy)
# 			db.session.commit()

# 			# mogle

# 			return redirect(url_for('academy'))

# 		return render_template('academy_create.html', .........., ..........)