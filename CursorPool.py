#!/usr/bin/python
# -*- coding: latin-1 -*-

def get_conexion():
    pass


class CursorPool():
    # metodo enter
    # Inicio del bloque with
    def __enter__(self):
            self.conn = get_conexion()
            self.cursor = self.conn.cursor()
            return self.__cursor
    # metodo exit
    # Fin del bloque with
    def __exit__(self, exception_type, exception_value, exception_traceback):
            if exception_value:
                    self.conn.rollback()
            else:
                    self.conn.commit()
            # Cerramos el cursor
            self.__cursor.close()
            # Regresar la conexi�n al pool
            liberar_conexion(self.conn)
