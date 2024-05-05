#Se importa la librería para gestionar la base de datos
import sqlite3

#Se establece el puente de conexión
conexion = sqlite3.connect("web2.sqlite3")
cursor = conexion.cursor()

#Eliminación previsora de de la tabla productos
cursor.execute("""
drop table if exists productos;
               """)

#Creación de la tabla productos
cursor.execute("""
create table if not exists productos (
               id interger primary key,
               categoria text not null,
               marca text not null,
               nombre text not null,
               descripcion text not null,
               precio interger not null
                );               
               """)

#Datos a insertar
productos_tecnologicos = [
    (100, "Smartphone", "Apple", "iPhone 13", "Chip A15 Bionic, pantalla Super Retina XDR.", 4000000),
    (200, "Laptop", "Dell", "XPS 13", "Ultrabook con procesador Intel Core i7 y pantalla InfinityEdge 4K.", 5850000),
    (300, "Tablet", "Samsung", "Galaxy Tab S7", "Tablet con pantalla AMOLED de 120Hz y S Pen incluido.", 2600000),
    (400, "Smartwatch", "Fitbit", "Versa 3", "Reloj inteligente con monitorización de actividad y ritmo cardiaco.", 900000),
    (500, "Cámara", "Canon", "EOS R6", "Cámara mirrorless con sensor full-frame y grabación de video 4K.", 9800000),
    (600, "Router", "Netgear", "Nighthawk AX8", "Router Wi-Fi 6 con 8 streams y velocidad de hasta 6 Gbps.", 170000),
    (700, "TV", "Sony", "Bravia XR A90J", "Televisor OLED 4K con procesador Cognitive Processor XR.", 9800000),
    (800, "Altavoz inteligente", "Amazon", "Echo Dot (4th Gen)", "Altavoz con asistente virtual Alexa y sonido mejorado.", 200000)
]

#Insertar datos
cursor.executemany("""
insert into productos values (?, ?, ?, ?, ?, ?);
                   """, productos_tecnologicos)

#Realizar y guardar cambios
conexion.commit()
conexion.close()