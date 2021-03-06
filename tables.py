from flask_table import Table, Col, LinkCol


class Tabla(Table):
    """docstring for Tabla"""
    username = Col("usuario")
    #password = Col("password")
    email = Col("email")
    id_usario = Col("representante id")
    id = Col("id")
    """
    para referencias futuras en el link col se establece un enlace 
    un td para el nombre de la columna el segundo argumento es para 
    hacer referencia a url_for donde vamos a indicar el nombre de la
    clase a la que vamos a redirigir, como atributo especial se parara
    un diccionario donde, pero se sentencia sera tratada como la de un 
    objeto normal la salida seria igual a la que tendiamos estableciendo
    usuario.nombre para el nombre del usuario. el diccionario que le sigue es
    para darle los estilos mediante clases css
    """
   # editar = LinkCol("editar", "edita",
    #                 url_kwargs=dict(id='id'),
     #                anchor_attrs={'class': 'btn btn-success'})
    #eliminar = LinkCol("eliminar", "borrar",
   #                  url_kwargs=dict(id='id'),
    #                 anchor_attrs={'class': 'btn btn-danger'})

class Alumnos(Table):
    """docstring for Alumnos"""
    nombre = Col("Nombre")
    apellido = Col("Apellido")
    cedula = Col("Cedula")
    escuela = Col("Escuela")
    edad = Col("Edad")

class items(object):
    """docstring for items"""
    def __init__(self, username,email, id_usario,id):
        self.username = username
        self.email = email
        self.id_usario =  id_usario
        self.id = id
        
        