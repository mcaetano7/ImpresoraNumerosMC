import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv 

# cargar variables de entorno

load_dotenv()

# cpnfig. base de datos
DB_HOST = os.getenv("localhost")
DB_USER = os.getenv("root")
DB_PASS = os.getenv("Carluncho.2004")
DB_NAME = os.getenv("ImpresoraNumerosMC")


def conectar():
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
            autocommit=False # better transaction management
            charset='utf8mb4' # ensure proper character encoding
        )
        if conexion.is_connected():
            print("Conexión exitosa")
        return conexion
    except Error as err:
        print(f"Error de conexión: {err}")
        return None
    
    def create_base_datos(): # crea la vase y tablas if not ecisrs
        try:
            conexion_temp = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASS
            )
            cursor = conexion_temp.cursor()

            # create databse if not exists
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            cursor.execute(f"USE {DB_NAME}")

            # crea la tabla si no existe
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS contador (
                    ID INT AUTO_INCREMENT PRIMARY KEY,
                    numero INT NOT NULL DEFAULT 0,
                    fecha_actualizacion TIMPESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                )
            """)

            