from conexion import conectar

conexion = conectar()
if conexion:
    cursor = conexion.cursor()
    cursor.execute("SELECT numero FROM contador ORDER BY id DESC LIMIT 1")
    numero_actual = cursor.fetchone()[0]
    print(f"Número actual: {numero_actual}")
    conexion.close()