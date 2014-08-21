# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import (
    StringField,
    PasswordField,
    TextAreaField
)
from wtforms import validators
from wtforms.fields.html5 import EmailField

class AcademyForm(Form):
	academy_name = StringField(
        u'학원이름',
        [validators.data_required(u'학원이름을 입력하시기 바랍니다.')],
        description={'placeholder': u'학원이름을 입력해주세요.'}
    )

    teacher_name = StringField(
        u'강사이름',
        [validators.data_required(u'강사이름을 입력하시기 바랍니다.')],
        description={'placeholder': u'강사이름을 입력해주세요.'}
    )

    academy_introduce = TextAreaField(
        u'학원소개',
        [validators.data_required(u'학원소개를 입력하시기 바랍니다.')],
        description={'placeholder': u'학원소개를 해주세요.'}
    )

    teacher_introduce = TextAreaField(
        u'강사소개',
        [validators.data_required(u'강사소개를 입력하시기 바랍니다.')],
        description={'placeholder': u'강사소개를 해주세요.'}
    )

    curriculum_introduce = TextAreaField(
        u'커리큘럼소개',
        [validators.data_required(u'커리큘럼소개를 입력하시기 바랍니다.')],
        description={'placeholder': u'커리큘럼을 안내해주세요.'}
    )

    academy_address = StringField(
        u'학원주소',
        [validators.data_required(u'학원주소를 입력하시기 바랍니다.')],
        description={'placeholder': u'학원주소를 입력해주세요.'}
    )

    welcome_line = StringField(
        u'환영인사',
        [validators.data_required(u'한줄인사를 입력하시기 바랍니다.')],
        description={'placeholder': u'한줄 환영인사를 입력해주세요.'}
    )

    phone_number = StringField(
        u'연락처',
        [validators.data_required(u'연락처를 입력하시기 바랍니다.')],
        description={'placeholder': u'연락처를 입력해주세요.'}
    )

    class_time = TextAreaField(
        u'수업시간',
        [validators.data_required(u'수업시간를 입력하시기 바랍니다.')],
        description={'placeholder': u'수업시간을 입력해주세요.'}
    )

    class_fee = StringField(
        u'수강료',
        [validators.data_required(u'수강료를 입력하시기 바랍니다.')],
        description={'placeholder': u'수강료를 입력해주세요.'}
    )

    homepage = StringField(
        u'홈페이지',
        [validators.data_required(u'홈페이지를 입력하시기 바랍니다.')],
        description={'placeholder': u'홈페이지를 입력해주세요.'}
    )