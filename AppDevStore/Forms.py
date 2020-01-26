from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, DecimalField, IntegerField, FileField

class CreateUserForm(Form):
    productName = StringField('Product Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    category = SelectField('Category', [validators.DataRequired()] , choices=[('', 'Select'),('B', 'Earbuds'), ('H', 'Headphones'), ('M', 'Microphones')], default='')
    brand = RadioField('Brand', [validators.DataRequired()], choices=[('B', 'Beats by Dre'), ('S', 'Sony'), ('R', 'Razer')], default='B')
    quantity = IntegerField('Quantity', [validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.Optional()])
