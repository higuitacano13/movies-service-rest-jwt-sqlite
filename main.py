from fastapi import Depends, FastAPI,  Path, Query, HTTPException # Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from movie import Movie
from user import User
from jwt_manager import create_token
from middlewares.jwt_bearer import JWTBearer
from config.database import Session, engine, Base
from models.movie import MovieModel
from middlewares.error_handler import ErrorHandler

# ========== Crear la aplicación ========== #
app = FastAPI()
app.title = "App con FastAPI" # -> Titulo de la documentación.
app.version = "0.0.1" # -> Versión de la documentación.
app.add_middleware(ErrorHandler) # -> Crear un sistema de manejo de errores.

# ========== Conexión a BD ========== #

Base.metadata.create_all(bind=engine)

# ================== Autenticación ====================== #

@app.post('/login', tags=['authentication'], status_code=200)
def login(user: User):
    try:
        if user.email == "jhiguitac@gmail.com" and user.password == "pass2024":
            token = create_token(dict(user))
        return JSONResponse(status_code=200, content={'Token': token})
    except Exception as error:
        raise Exception(error)

# ================== Consultar Peliculas ====================== #

@app.get('/movies', tags=['Movies'], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies():
    try:
        db = Session()
        result = db.query(MovieModel).all()
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    except Exception as error:
        return HTTPException(status_code=500, content=str(error))

# ================== Consultar Peliculas por Id ====================== #

@app.get('/movies/{id}', tags=['Movies'], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movie_by_id(id: int = Path(ge=1)):
    try:
        db = Session()
        result = db.query(MovieModel).filter(MovieModel.id == id).first()
        if not result:
            raise HTTPException(status_code=404, content={"Message": 'Movie not found'})
        else:
            return JSONResponse(status_code=200,content=jsonable_encoder(result))
    except Exception as error:
        raise HTTPException(status_code=500, content={"Message": str(error)})
        
# ================== Consultar Peliculas por Categoria ====================== #

@app.get('/movies/', tags=['Movies'], dependencies=[Depends(JWTBearer())])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    try:
        db = Session()
        result = db.query(MovieModel).filter(MovieModel.category == category).all()
        if not result:
            raise HTTPException(status_code=404, detail={"Message": 'Movie not found'})
        else:
            return JSONResponse(status_code=200,content=jsonable_encoder(result))
    except Exception as error:
        raise HTTPException(status_code=500, content={"Message": str(error)})
    
# ================== Crear Nueva Película ====================== #

@app.post('/movies/', tags=['Movies'], status_code=201, dependencies=[Depends(JWTBearer())])
def create_movies(movie: Movie):
    try:
        db = Session()
        new_movie = MovieModel(**movie.model_dump())
        db.add(new_movie)
        db.commit()
        return JSONResponse(status_code=201, content={'Message': "Se ha guardado el registro exitosamente"})
    except Exception as error:
        raise HTTPException(status_code=500, content=str(error))

# ================== Modificar Película ====================== #
    
@app.put('/movies/{id}', tags=['Movies'], status_code=200, dependencies=[Depends(JWTBearer())])  
def update_movie( id: int, movie: Movie):
    try:
        db = Session()
        result = db.query(MovieModel).filter(MovieModel.id == id).first()
        if not result:
            raise HTTPException(status_code=404, content={"Message": 'Movie not found'})
        else:
            result.title = movie.title if movie.title is not None else result.title
            result.overview = movie.overview if movie.overview is not None else result.overview
            result.year = movie.year if movie.year is not None else result.year
            result.category = movie.category if movie.category is not None else result.category
            result.rating = movie.rating if movie.rating is not None else result.rating
            db.commit()
            return JSONResponse(status_code=200, content={'Message': "Se ha editado el registro exitosamente"})
    except Exception as error:
        raise HTTPException(status_code=500, content=str(error))
    

# ================== Eliminar Película ====================== #
    
@app.delete('/movies/{id}', tags=['Movies'], status_code=200, dependencies=[Depends(JWTBearer())])
def delete_movie(id: int):
    try:
        db = Session()
        result = db.query(MovieModel).filter(MovieModel.id == id).first()
        if not result:
            raise HTTPException(status_code=404, content={"Message": 'Movie not found'})
        else:
            db.delete(result)
            db.commit()
            return JSONResponse(status_code=200, content={'Message': "Se ha eliminado el registro exitosamente"})
    except Exception as error:
        raise HTTPException(status_code=500, content=str(error))



