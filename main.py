from conexion import conectar

conexion = conectar()

if conexion:
    cursor = conexion.cursor()
    cursor.execute("SELECT numero FROM contador ORDER BY id DESC LIMIT 1")
    resultado = cursor.fetchone()
    if resultado:
        print(f"Número actual: {resultado[0]}")
    else:
        print("No hay datos en la tabla.")
    conexion.close()
else:
    print("No se pudo conectar. Verificá el archivo .env")
