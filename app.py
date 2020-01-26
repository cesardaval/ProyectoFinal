from flask import Flask
from flask import render_template, request, session
from flask import redirect, url_for
from flask import flash
from config import Configuracion_desarrollo
from models import User, db, Representante, Preinscripcion
from tables import Tabla, items
import forms
app = Flask(__name__)
app.config.from_object("config.Configuracion_desarrollo")


@app.route('/')
def inicio():

    if 'username' in session:
        print(session)
        return "estas logeado"
    return "inicio"

@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/mision')
def mision():
	return render_template("mision.html")

@app.route('/historia')
def historia():
	return render_template("historia.html")

@app.route('/registro')
def registro():
    form = forms.Formulario()
    return render_template("registro.html",forms = form)

@app.route('/reporte')
def reporte():

    item = [items("Maria", "correo@yahoo.com", "loca", "1"),]
    tabla = Tabla(item)
    return render_template("reporte.html", tabla = tabla)
    
if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()