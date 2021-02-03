##DIF METODOS
def fetchOne(cursor):
    # Es posible hacer una consulta que sólo retorne un registro. Para hacer eso, además de modificar la consulta se utiliza el método .fetchone().
    # %s es un comodín que será reemplazado
    sql = 'SELECT * FROM persona WHERE id_persona = %s'

    # id_persona es el valor que deberá de tener el comodín
    id_persona = 1
    # Para que el método .execute() ejecute de forma correta la query los valores deberán de ser una tupla, es por eso que el id_persona es convertido a tupla
    llave_primaria = (id_persona,)

    # Ejecuta la sentencia, reemplazando el comodín por el valor de llave_primaria
    cursor.execute(sql, llave_primaria)
    # Se guarda en una variable el retorno de .fetchone()
    registros = cursor.fetchone()
    return registros

def fetchAll(cursor):
    # También se puede seleccionar varios registros apoyándonos del .fetchall(), pero sin traernos toda la información de la tabla y haciendo uso de la palabra reservada IN en la sentencia.
    # IN permite incluir más de un dato
    sql = 'SELECT * FROM persona WHERE id_persona IN %s'

    # Como es más de un valor en este caso se necesita una tupla de tuplas
    llaves_primarias = ((1, 2, 3),)

    cursor.execute(sql, llaves_primarias)
    # Retorna todos los registros que coincidan con la busqueda
    registros = cursor.fetchall() 
    return registros

## OBTENER REGISTROS
# Una vez ejecutada la sentencia SQL, se necesita retornar la información proveniente de dicha sentencia hacemos uso del método .fetchall(), que también es propio de cursor. Este método retorna todo el contenido de la tabla a la que estamos accediendo.
registros = cursor.fetchall()
print(registros)

# Es posible hacer una consulta que sólo retorne un registro. Para hacer eso, además de modificar la consulta se utiliza el método .fetchone().
print(fetchOne(cursor))

# También se puede seleccionar varios registros apoyándonos del .fetchall(), pero sin traernos toda la información de la tabla y haciendo uso de la palabra reservada IN en la sentencia.
print(fetchAll(cursor))