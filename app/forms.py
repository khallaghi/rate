from wtforms import Form, BooleanField, TextField, PasswordField,SelectField,RadioField,validators, IntegerField, FileField
class FacultyForm(Form):
	name = TextField('Faculty name', [validators.Length(min=4, max=25)])
	uni = SelectField('University')

class ProfessorForm(Form):
	name = TextField('Professor name', [validators.Length(min=2, max=100)])
	family = TextField('Professor family', [validators.Length(min=2, max=100)])
	email = TextField('Email address')
	website = TextField('website')
	faculty = RadioField(' faculty ',coerce=unicode)
	room_no = TextField('room number')
	rank = RadioField('rank')
	pic = FileField(u'Image File')
	# uni = SelectField('University')
class SearchForm(Form):
	search = TextField('search it')

class ProfRateForm(Form):
	clarity = IntegerField('Clarity', [validators.NumberRange(min=0, max=5)])
	easyness = IntegerField('Easyness', [validators.NumberRange(min=0, max=5)])
	helpfullness = IntegerField('Helpfullness', [validators.NumberRange(min=0, max=5)])
	study = TextField('Study', [validators.Length(min=4, max=25)])
	is_online = RadioField('online ? ')
	coolness = RadioField('Coolness')
	attendance = RadioField('Attendance')
	take_it_again = RadioField('take it again')
	course_axis = RadioField('Course Axis')
	excercises = RadioField('Excercises')
	Exam = RadioField('What about exam')
	scale = RadioField('anything about scaling')
	project = RadioField('what about course projects')
	hardness = RadioField('course hardness')
	gradign = RadioField('what about grading')
	
	
	
	
	
	