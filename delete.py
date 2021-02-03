## Eliminar Registros
# Otra acción que es posible realizar es eliminar los registros. Para eliminarlos, la sentencia hace uso de la palabra reservada DELETE.
sql = 'DELETE FROM persona WHERE id_persona = %s'
# El comando DELETE siempre debe de ir acompañador de un WHERE, ya que si no se hace de esta forma se eliminarían todos los registros de la tabla por completo.

# De igual forma que para actualizar o insertar registros se hace uso del siguiente código para ejecutar y hacer persistente los cambios en la base de datos.
valores = (9,)
cursor.execute(sql, valores)
conexion.commit()