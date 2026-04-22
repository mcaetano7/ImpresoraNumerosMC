# ImpresoraNumerosMC

Sistema de turnos para locales con múltiples vendedores. Muestra el número de turno actual en una ventana pequeña y siempre visible en cada PC, actualizada en tiempo real. Cualquier PC puede avanzar, retroceder o resetear el turno.

---

## Requisitos

- Python 3.8 o superior
- Una base de datos MySQL accesible desde internet (ver opciones abajo)

---

## 1. Base de datos en la nube (hacerlo una sola vez)

Necesitás una base de datos MySQL accesible desde todas las PCs del local. Opciones gratuitas recomendadas:

### Opción A — Railway (recomendada, más fácil)
1. Entrá a [railway.app](https://railway.app) y creá una cuenta
2. Nuevo proyecto → **Deploy MySQL**
3. Hacé clic en el servicio MySQL → pestaña **Connect**
4. Copiá los datos: host, puerto, usuario, contraseña y nombre de la base de datos

### Opción B — PlanetScale
1. Entrá a [planetscale.com](https://planetscale.com) y creá una cuenta
2. Creá una base de datos → conectate con los datos que te dan

---

## 2. Instalación en cada PC

### Paso 1 — Clonar el repositorio
```bash
git clone https://github.com/mcaetano7/ImpresoraNumerosMC.git
cd ImpresoraNumerosMC
```

### Paso 2 — Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 3 — Configurar la conexión
1. Copiá el archivo `.env.example` y renombralo a `.env`
2. Completá con los datos de tu base de datos:

```
DB_HOST=tu-host
DB_PORT=3306
DB_USER=tu-usuario
DB_PASS=tu-contraseña
DB_NAME=ImpresoraNumerosMC
```

### Paso 4 — Crear la base de datos (solo en UNA PC, una sola vez)
```bash
python conexion.py
```
Esto crea la tabla y el registro inicial en la nube.

### Paso 5 — Ejecutar la aplicación
```bash
python ventana.py
```

O usando el acceso directo:
```bash
start.bat   # en Windows
```

---

## Uso

| Botón | Acción |
|-------|--------|
| ▶ | Avanzar al siguiente turno |
| ◀ | Retroceder al turno anterior |
| ↺ | Resetear a 0 (pide confirmación) |

La ventana se actualiza automáticamente cada segundo. Si otra PC cambia el número, todas lo ven al instante.

---

## Solución de problemas

**"Error de conexión"** → Verificá que el `.env` tenga los datos correctos y que la base de datos esté activa.

**El número no se actualiza** → Verificá la conexión a internet y que el host en `.env` sea el correcto.

**"No se pudo actualizar el número"** → Puede ser un problema de permisos en la base de datos. Verificá que el usuario tenga permisos de lectura y escritura.
