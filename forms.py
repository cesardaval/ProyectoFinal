from wtforms import Form
from wtforms import TextField
from wtforms import validators
from wtforms import PasswordField
from wtforms.fields.html5 import EmailField
from models import User


class Formulario(Form):
    """docstring for Formulario"""
    username = TextField('Usuario', [validators.length(
        min=8, max=25, message="ingrese un usuario valido"),
        validators.required(message='el campo es requerido')]
    )
    password = PasswordField('Password', [validators.length(
        min=8, max=25, message="ingrese una pasword valida"),
        validators.required(message='el campo es requerido')]
    )
    email = EmailField('Correo electronico', [validators.required(
        message="el correo es requerido")]
    )
    nombre = TextField('nombre', [validators.length(
        min=3, max=20, message="ingrese un nombre valido")])
    cedula = TextField('Cedula', [validators.length(
        min=6, max=12, message="ingrese una cedula valida")])

    def validate_username(form, field):
        username = field.data
        user = User.query.filter_by(username=username).first()
        if user is not None:
            raise validators.ValidationError(
                "El usuario ya se encuentra registrado.")

    def validate_cedula(form, field):
        cedula = field.data
        user = User.query.filter_by(cedula=cedula).first()
        if user is not None:
            raise validators.ValidationError(
                "La cedula ya se encuentra registrada.")


class loggin(Form):
    """docstring for loggin"""
    username = TextField('Usuario',
                         [validators.length(min=8, max=25),
                          validators.required(
                              message='el usuario es requerido')
                          ])
    password = PasswordField('Password', [validators.length(min=8, max=95),
                                          validators.required(message="el usuario es requerido")])


class RegistroAlumno(Form):
    """docstring for RegistroAlumno"""

    nombre = TextField('Nombre', [validators.length(
        min=3, max=20, message="ingrese un nombre valido"),
        validators.required(message="el usuario es requerido")])

    apellido = TextField('Apellido', [validators.length(
        min=3, max=20, message="ingrese un nombre valido"),
        validators.required(message="el usuario es requerido")])

    escuela = TextField('Escuela', [validators.length(
        min=8, max=50, message="ingrese un nombre valido"),
        validators.required(message="el usuario es requerido")])

    edad = TextField('Edad', [validators.length(
        min=1, max=3, message="ingrese un nombre valido"),
        validators.required(message="la Edad del Estudiante es requerida")])

    cedula = TextField('Cedula', [validators.length(
        min=8, max=8, message="ingrese una cedula valida"),
        validators.required(message="la cedula del estudiante es requerida")])

    def validate_cedula(form, field):
        cedula = field.data
        user = User.query.filter_by(cedula=cedula).first()
        if user is not None:
            raise validators.ValidationError(
                "La cedula ya se encuentra registrada.")

    def validate_edad(form, field):
        edad = int(field.data)
        if edad < 9 or edad > 20:
            raise validators.ValidationError(
                "Revise la edad introducida.")
