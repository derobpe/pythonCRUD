#!/usr/bin/python
# -*- coding: latin-1 -*-

import psycopg2

# CREAR CONEXIÓN a la DB
conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
)

## Manejo de Transacciones
# Cuando se trabaja con transacciones: o se guardan todos los cambios realizados a la base de datos o no se guarda ninguno de ellos.

# La sentencia SELECT no es necesario que esté dentro de una transacción, pero puede participar en ella.

# Ejemplo de manejo de transacciones:
try:
    cursor = conexion.cursor()
    sql = 'INSERT INTO persona(id, nombre, apellido, email) values(%s, %s, %s, %s)'
    valores = (2, 'Carolina2', 'Ortiz2', 'carolina2@gmail.com')

    # Ejecución de la sentencia
    cursor.execute(sql, valores)
        # Hacer persistentes los cambios en la base de datos
    conexion.commit()
except Exception as e:
    # rollback da marcha atras a todas las operaciones pendientes en caso de que alguna falle
    conexion.rollback()
    print(f'Ocurrio un error en la transacción: {e}')
finally:
    # Cierre de conexión y cursor
    cursor.close()
    conexion.close()