from flask import Flask
from flask import render_template, request, session
from flask import redirect, url_for
from flask import flash
from flask_weasyprint import HTML, render_pdf
from config import Configuracion_desarrollo
from models import User, db, Representante, Preinscripcion
from tables import Alumnos
import forms
app = Flask(__name__)
app.config.from_object("config.Configuracion_desarrollo")


@app.before_request
def before_request():
    if 'username' not in session and request.endpoint in ['perfil', 'preinscripcion', 'reporte']:
        return redirect(url_for('login'))
    if 'username' in session and request.endpoint in ['registro', 'login']:
        return redirect(url_for("perfil"))


@app.route('/')
def inicio():

    return render_template("index.html")


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/mision')
def mision():
    return render_template("mision.html")


@app.route('/historia')
def historia():
    return render_template("historia.html")


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    """
    esta ruta da el formulario de registro.

    """
    # objeto formulario para pasarlo a jinja2
    form = forms.Formulario(request.form)
    # si la respuesta del formulario es de tipo post y si no tiene errores
    # entonces crea una instancia Users y rellena para agregarlo a la base
    # la tabla Users
    if request.method == 'POST' and form.validate():
        user = User(form.nombre.data, form.cedula.data,
                    form.username.data, form.email.data,
                    form.password.data)
        db.session.add(user)
        db.session.commit()
    return render_template("registro.html", forms=form)


@app.route('/reporte')
def reporte():

    repre = User.query.filter_by(id=session['user_id']).first()
    alunmos = db.session.query(Representante,
                               Preinscripcion
                               ).join(Preinscripcion).filter_by(id_Representante=session['user_id']).add_columns(
        Preinscripcion.nombre, Preinscripcion.apellido,
        Preinscripcion.cedula, Preinscripcion.escuela,
        Preinscripcion.edad)
    tabla = Alumnos(alunmos)
    chtml = render_template("reporte.html", tabla=tabla, repre=repre)
    return render_pdf(HTML(string=chtml))


@app.route('/loggin', methods=['GET', 'POST'])
def login():
    hola = forms.loggin(request.form)
    if request.method == 'POST'and hola.validate():
        username = hola.username.data
        password = hola.password.data
        user = User.query.filter_by(username=username).first()
        if user is not None and user.comparar(password):
            susseces_message = "bienbenido{}".format(username)
            flash(susseces_message)
            session['username'] = username
            session['user_id'] = user.id
            return redirect(url_for("Representantes"))
        else:
            error_message = "usuario o contraseña invalida"
            flash(error_message)

    return render_template("loggin.html", forms=hola)


@app.route('/preinscripcion', methods=['GET', 'POST'])
def preinscripcion():
    registro = forms.RegistroAlumno(request.form)
    id_representante = Representante.query.get(session['user_id'])
    if request.method == 'POST' and registro.validate():
        preInscrito = Preinscripcion(nombre=registro.nombre.data,
                                     apellido=registro.apellido.data,
                                     escuela=registro.escuela.data,
                                     edad=registro.edad.data,
                                     Representantes=id_representante,
                                     cedula=registro.cedula.data)
        db.session.add(preInscrito)
        db.session.commit()
    return render_template("preinscripcion.html", forms=registro)


@app.route('/perfil')
def perfil():
    perfil = User.query.filter_by(id=session['user_id']).first()
    return render_template("perfil.html", perfil=perfil)


@app.route("/Representantes")
def Representantes():
    """
    esta ruta es para guardar los datos la repesentantes de manera automatica
    si todo esta bien no tienen que percatarse de lo que esta pasando :V

    nota para mi yo del futuro, te acabas de encontrar de casualidad una situacion
    no esperada, programamos la tabla de representantes para que sea igual 
    id tabla y el id_relacion y sin querer hice un registro que rompiera con esta 
    logica y a la hora de lanzar el reporte da como resultado un intercambio de datos
    porfavor recuerda sulucionarlo en el futuro gracias <3 recuerda que fue 1 2
    y 2 1
    """
    # objeto consulta que filtra si el usuario esta en la tabla Representantes
    representante = Representante.query.filter_by(
        id_usuario=session['user_id']).first()

    # objeto consulta que obtiene el id del usuario segun el id que tiene
    # en la session
    user = User.query.get(session['user_id'])

    if representante is None:
        print(representante)
        print(user)
        r = Representante(Users=user)
        db.session.add(r)
        db.session.commit()
        return redirect(url_for('perfil'))

    elif representante.id_usuario == user.id:
        return redirect(url_for('perfil'))

    print(representante)
    print(user)
    return redirect(url_for('perfil'))


@app.route('/salir')
def salir():
    """
    esta ruta es para eliminar la cookie session

    """
    if 'username' in session:
        session.pop('username')
    return redirect(url_for("login"))


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
