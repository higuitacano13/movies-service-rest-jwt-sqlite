# 🎬 Movies API REST con JWT & SQLite

Movies Service REST es una API construida con FastAPI que permite realizar operaciones CRUD sobre una base de datos de películas. Incluye autenticación y autorización mediante JSON Web Tokens (JWT) para proteger los endpoints, garantizando así que solo los usuarios autenticados puedan acceder o modificar los datos.

# 🚀 Tecnologías utilizadas
- **FastAPI** – Framework moderno y rápido para la creación de APIs con Python.
- **SQLite** – Base de datos relacional ligera para almacenamiento local.
- **SQLAlchemy** – ORM para trabajar con bases de datos de forma declarativa.
- **PyJWT** – Librería para codificar y decodificar JWT.

# ⚙️ Funcionalidades
**1. Autenticación con JWT**
  - Generación de tokens al iniciar sesión.
  - Verificación de tokens en rutas protegidas.
  - Expiración configurable para los tokens.
    
**2.CRUD de Películas (Entidad: Movie)**
  - Crear película (POST /movies)
  - Obtener todas las películas (GET /movies)
  - Obtener una película por ID (GET /movies/{id})
  - Actualizar película (PUT /movies/{id})
  - Eliminar película (DELETE /movies/{id})
  - Todas las operaciones están protegidas con JWT.
    
**3. Gestión de usuarios (básico)**
  - Registro de nuevos usuarios.
  - Inicio de sesión para obtener el token JWT.

# ✅ Requisitos del entorno
- Python 3.8+
- pip (gestor de paquetes de Python)
- Entorno virtual (opcional pero recomendado)
