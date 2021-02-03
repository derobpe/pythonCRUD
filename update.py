## Actualizar Registros
# Para actualizar registros dentro de la base de datos se modifica la sentencia SQL y en lugar se hacer uso del SELECT o INSERT, utilizamos la palabra reservada UPDATE.
sql = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona  = %s'
# De igual forma se genera la tupla con los valores que se desean modificar.
valores = ('Carlos2', 'Lara2', 'carlos2@gmail.com', 8)
# Y se ejecuta la sentencia guardando los cambios en la base de datos.
cursor.execute(sql, valores)
conexion.commit()
# Es posible también actualizar más de un registro al mismo tiempo. De nuevo esto es hecho a través de una tupla de tuplas.
valores = (
    ('Carlos', 'Lara', 'carlos@gmail.com', 8),
    ('Julio2', 'de la Torre2', 'julio2@gmail.com', 9),
)
# Y haciendo uso del .executemany().
cursor.executemany(sql, valores)
conexion.commit()