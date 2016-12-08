from flask.ext.wtf import Form
from wtforms.fields import TextField
from wtforms.validators import Required

#Fields are defined as members on a form in a declarative fashion:
class TODOFORM(Form):
	label = TextField('label', validators = [Required()])
	
