# # MySQL
# pip3 install mysql-connector-python
# # PostgreSQL
# pip3 install psycopg2-binary

# Ejemplo importando PostgreSQL
import psycopg2
import fetch



# CREAR CONEXIÓN a la DB
conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
)

## CURSORES
# Para ejecutar sentencias hacia la base de datos se hace uso del cursor
cursor = conexion.cursor()
# Como el cursor nos permite ejecutar las sentencias, es necesario crear dicha sentencia. También se recomienda crearlas en una variable para facilitar su uso.
sql = 'SELECT * FROM persona'
# Para ejecutarla se utiliza el método .execute() propio del cursor.
cursor.execute(sql)




# CERRAR CONEXIÓN
# Cuándo la conexión (y por ende el cursor) van a dejar de ser usados, se deben de cerrar. Esto se realiza a través del método .close(). Dicho método aplica tanto para la conexión como para el cursor.
cursor.close()
conexion.close()