## INSERTAR REGISTROS
# Para insertar nuevos registros dentro de la base de datos se modifica la sentencia SQL y en lugar se hacer uso del SELECT se debe de utilizar INSERT.
sql = 'INSERT INTO persona(nombre, apellido, email) values(%s, %s, %s)'
# De igual forma se debe de crear una tupla con los valores que reemplazaran los comodines de la sentencia.
valores = ('Carlos', 'Lara', 'carlos@gmail.com')
# También se hace uso del cursor para ejecutar la inserción de datos, pero como no se esta leyendo la información de la base de datos sino que se quiere guardar información nueva dentro de ella, se debe de hacer uso del método .commit() para que queden guardados los nuevos datos.
cursor.execute(sql, valores)
# Guardar la información en la bade de datos
conexion.commit()

# cursor.rowcount cuenta cuantos registros se insertaron y se guarda en la variable registros_insertados
registros_insertados = cursor.rowcount

# Se puede ingresar más de un registro al mismo tiempo. Esto se hace creando una tupla de tuplas con los valores a insertar.
valores = (
    ('Carlos', 'Lara', 'carlos@gmail.com'),
    ('Julio', 'de la Torre', 'julio@gmail.com'),
    ('Carolina', 'Ortiz', 'carolina@gmail.com')
)
# Pero para ejecutar la sentencia se hace uso del método .executemany().
cursor.executemany(sql, valores)
conexion.commit()