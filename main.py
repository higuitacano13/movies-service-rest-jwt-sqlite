from fastapi import FastAPI
from config.database import engine, Base
from routers.movie_router import movie_router
from routers.user_router import user_router
from middlewares.error_handler import ErrorHandler

# ========== Crear la aplicación ========== #
app = FastAPI()
app.title = "App con FastAPI" # -> Titulo de la documentación.
app.version = "0.0.1" # -> Versión de la documentación.
# app.add_middleware(ErrorHandler) # -> Crear un sistema de manejo de errores.

app.include_router(movie_router)
app.include_router(user_router)

# ========== Conexión a BD ========== #
Base.metadata.create_all(bind=engine)


