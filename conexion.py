import mysql.connector

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'T3ddy2013,santibueno'
DB_NAME = 'IMPRESORA'

def conectar():
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None