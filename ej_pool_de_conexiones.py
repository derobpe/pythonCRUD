#!/usr/bin/python
# -*- coding: utf8 -*-

import psycopg2
import CursorPool

# CREAR CONEXION a la DB
conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
)

# Pool de Conexiones
# Un pool de conexiones es una clase que a su vez administra las conexiones a nuestra base de datos y puede almacenar varias conexiones a la base de datos.

# Diagrama 1.2: Pool de Conexiones en Python

# Al crear un pool de conexiones se establece el min y max de conexiones que va a poder admitir. No es posible pasar del máximo de conexiones permitidas del pool.

# Psycopg2 ya contiene métodos para trabajar con el pool de conexiones. Para trabajar con ellos se debe de importar de la siguiente manera:
from psycopg2 import pool
# Para crear un pool de conexiones se hace uso de la importación anterior que contiene el metodo SimpleConnectionPool. Este m�todo recibe el m�nimo y m�ximo de conexiones permitidas, as� como tambi�n todos los demás datos necesarios para establecer la conexión.
poolConexiones = pool.SimpleConnectionPool(
    1,
    5,
    user        = 'postgres',
    password    = 'admin',
    host        = '127.0.0.1',
    port        = '5432',
    database    = 'test_db'
)
# Una vez creado el pool de conexiones, se puede hacer uso de una de estas utilizando el m�todo .getconn().
conexion = poolConexiones.getconn()

# Cuando se termine de trabajar con la conexión previamente asignada, esta debe de regresar al pool para estar disponible en caso de que se requiera usar de nuevo. El m�todo .putconn() permite liberar la conexión en uso.
poolConexiones.putconn(conexion)

## TODO seguir!
# clase CursorPool() que contiene dos metodos __enter__ y __exit__. Esos dos métodos son invocados por el with en ese orden, lo que facilita la ejecución de sentencias y la liberación de las conexiones.
# Para crear cursores con un pool de conexiones 
with CursorPool() as cursor:
    pass


# Cuando se termina de trabajar con la base de datos se utiliza el metodo .closeall() para cerrar el pool y todas sus conexiones.
poolConexiones.closeall()