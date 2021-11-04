import os
import sqlite3
from sqlite3 import Error

from constantes import RECURSOS


def create_table(connection):
    """
    Crea la tabla y le inserta valores en caso de que no exista o esté vacía.

    :param connection: conexión con la base de datos
    """
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS puntos (hight_score INTEGER)')
    cons = cursor.execute('SELECT * FROM puntos').fetchall()
    if len(cons) == 0:
        cursor.execute('INSERT INTO puntos VALUES (0)')
    connection.commit()


def create_connection():
    """
    Crea la conexión con la base de datos

    :return: conexión
    """
    conn = None
    try:
        conn = sqlite3.connect(os.path.join(RECURSOS, "PyShip.db"))

        create_table(conn)
    except Error as e:
        print(e)
    return conn


class Database:
    def __init__(self):
        """
        Constructor de la clase Database
        Almacena la conexión de la base de datos que se conecta cuando se crea el objeto.
        """
        self.conn = create_connection()

    def get_score(self):
        """
        Obtiene el score almacenado en la base de datos

        :return: score
        """
        cursor = self.conn.cursor()
        res = cursor.execute('SELECT hight_score FROM puntos').fetchone()
        return res[0]

    def update_score(self, high_score):
        """
        Actualiza la puntuación de la base de datos

        :param high_score: nuevo high score
        """
        cursor = self.conn.cursor()
        cursor.execute('UPDATE puntos set hight_score={}'.format(high_score))
        self.conn.commit()
