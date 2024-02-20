from fastapi import APIRouter, HTTPException, Depends, Path, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schema.movie_schema import Movie
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from services.movie_service import MovieService


movie_router = APIRouter()


# ================== Consultar Peliculas ====================== #

@movie_router.get('/movies', tags=['Movies'], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies():
    try:
        db = Session()
        result = MovieService(db).get_movies()
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    except Exception as error:
        return HTTPException(status_code=500, detail=str(error))

# ================== Consultar Peliculas por Id ====================== #

@movie_router.get('/movies/{id}', tags=['Movies'], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movie_by_id(id: int = Path(ge=1)):
    try:
        db = Session()
        result = MovieService(db).get_movie_by_id(id)
        if not result:
            raise HTTPException(status_code=404, detail={"Message": 'Movie not found'})
        else:
            return JSONResponse(status_code=200,content=jsonable_encoder(result))
    except Exception as error:
        raise HTTPException(status_code=500, detail={"Message": str(error)})
        
# ================== Consultar Peliculas por Categoria ====================== #

@movie_router.get('/movies/', tags=['Movies'], dependencies=[Depends(JWTBearer())])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    try:
        db = Session()
        result = MovieService(db).get_movies_by_category(category)
        if not result:
            raise HTTPException(status_code=404, detail={"Message": 'Movie not found'})
        else:
            return JSONResponse(status_code=200,content=jsonable_encoder(result))
    except Exception as error:
        raise HTTPException(status_code=500, detail={"Message": str(error)})
    
# ================== Crear Nueva Película ====================== #

@movie_router.post('/movies/', tags=['Movies'], status_code=201, dependencies=[Depends(JWTBearer())])
def create_movies(movie: Movie):
    try:
        db = Session()
        MovieService(db).create_movies(movie)
        return JSONResponse(status_code=201, content={'Message': "Se ha guardado el registro exitosamente"})
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

# ================== Modificar Película ====================== #
    
@movie_router.put('/movies/{id}', tags=['Movies'], status_code=200, dependencies=[Depends(JWTBearer())])  
def update_movie( id: int, movie: Movie):
    try:
        db = Session()
        result = MovieService(db).get_movie_by_id(id)
        print(f'El resultado es: {result}')
        if result is None:
            raise HTTPException(status_code=404, detail={"Message": 'Movie not found'})
        MovieService(db).update_movie(movie, id)
        return JSONResponse(status_code=200, content={'Message': "Se ha editado el registro exitosamente"})
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
    

# ================== Eliminar Película ====================== #
    
@movie_router.delete('/movies/{id}', tags=['Movies'], status_code=200, dependencies=[Depends(JWTBearer())])
def delete_movie(id: int):
    try:
        db = Session()
        result = MovieService(db).get_movie_by_id(id)
        if not result:
            raise HTTPException(status_code=404, detail={"Message": 'Movie not found'})
        else:
            MovieService(db).delete_movie(id)
            return JSONResponse(status_code=200, content={'Message': "Se ha eliminado el registro exitosamente"})
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))



