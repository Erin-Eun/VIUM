from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

# 웹 브라우저에서 서버로 전송된 폼을 처리할 때 사용
class UserLoginForm(FlaskForm):
    branch = StringField('지점명', validators=[DataRequired(), Length(max=10)])
    username = StringField('사용자이름', validators=[DataRequired(), Length(max=10)])
    password = PasswordField('비밀번호', validators=[DataRequired()])