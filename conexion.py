import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT", 3306))


def conectar():
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
            autocommit=False,
            charset='utf8mb4'
        )
        if conexion.is_connected():
            print("Conexión exitosa")
            return conexion
    except Error as err:
        print(f"Error de conexión: {err}")
        return None


def crear_base_de_datos():
    """Crea la base de datos y la tabla si no existen. Ejecutar una sola vez."""
    try:
        conexion_temp = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASS,
            charset='utf8mb4'
        )
        cursor = conexion_temp.cursor()

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        cursor.execute(f"USE {DB_NAME}")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contador (
                id INT AUTO_INCREMENT PRIMARY KEY,
                numero INT NOT NULL DEFAULT 0,
                fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            )
        """)

        # Insertar fila inicial si la tabla está vacía
        cursor.execute("SELECT COUNT(*) FROM contador")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO contador (numero) VALUES (0)")

        conexion_temp.commit()
        print("Base de datos y tabla creadas correctamente.")
        cursor.close()
        conexion_temp.close()

    except Error as err:
        print(f"Error al crear la base de datos: {err}")


if __name__ == "__main__":
    crear_base_de_datos()
