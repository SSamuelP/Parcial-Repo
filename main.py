from flask import Flask, render_template, redirect
import sqlite3
from pprint import pprint

#Conexión con la base de datos
conexion = sqlite3.connect("web2.sqlite3")
conexion.row_factory = sqlite3.Row

#Cargamos los datos mediante consulta y los convertimos en diccionarios
cursor = conexion.cursor()
cursor.execute("""
select * from productos;
               """)

productos = [ dict(producto) for producto in cursor.fetchall() ]
#pprint(productos)

cursor.close()
conexion.close()

#Creamos la aplicación
app = Flask(__name__)

#Rutas

@app.route("/")
def inicio():
    return render_template('index.html', productos = productos)

#Ruta cada producto
@app.route("/producto/<int:pid>")
def ruta_producto(pid):
    for producto in productos:
        if pid == producto['id']:
            return render_template('producto.html', producto = producto)
    return redirect("/")
#Ejecución del programa
if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)