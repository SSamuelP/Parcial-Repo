# Proyecto: Página web con flask

## ¿Cómo funciona?:

- Mediante la creación de una base de datos con el modulo _sqlite3_ se crea una base de datos. En ella se crea una tabla _productos_ y se ingresan 6 columnas (id, categoria, marca, nombre, descripción y precio).
- Se ingresa una lista de tuplas, las cuales contienen la información para cada una de esas columnas, y se llena la tabla a partir de esta lista. **Recalcar que si los datos son cambiados, aún así podrá funcionar y no dará problemas.**
- El modulo Flask nos ayudará a conectarnos con la base de datos creada y nos permitirá acceder a los datos de la misma.
- Para proceder con el display de esta página web haremos 3 archivos html, los cuales nos servirán para dar forma a la página.
  1. El primero de ellos es ```base.html```. Este es el documento que usaremos como fundamento para la creación de las otras páginas, en ella ponemos los elementos que queremos que estén en todos los archivos.
  2. El segundo de ellos es ```index.html```. Este archivo contiene la estructura del listado de productos que tenemos en nuestra base de datos.
  3. El tercero es ```producto.html```. El cual tiene la estructura de la página individual para cada producto, y un boton de inicio.
- Y mediante la creación de una carpeta _static_, subiremos la estructura del formato visual de cada página. En ella encontraremos el archivo ```estilos.css```, en ella estarán definidos los componentes visuales de las páginas, como lo es el fondo de la página, etc. Y los otros elementos son las fotos de los productos con el nombre cambiado al id de cada producto. Esto con el fin de que al momento de poder relacionar las imagenes con nuestros objetos en la base de datos. Y también el logo de la tienda.

## Ejecución:
La ejecución de este programa se debe de hacer e n un orden en específico, ya que primero se debe ejecutar el archivo ```crear_db.py```, el cual creará la base de datos y la tabla con los datos.
Seguido de esto se ejecuta el archivo princípal ```main.py```, en el cual se ejecutarán las distintas páginas, así como las plantillas necesarias para poder ver imagenes y otros elementos visuales.

## Creador:
Samuel Santiago Pinzón Reina
Cuarto semestre
Ingeniería de sistemas
