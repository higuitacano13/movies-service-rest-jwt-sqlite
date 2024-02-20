from models.movie_model import MovieModel
from fastapi import HTTPException
from schema.movie_schema import Movie

class MovieService():

    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie_by_id(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    
    def get_movies_by_category(self, category):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result

    def create_movies(self, movie: Movie):
        new_movie = MovieModel(**movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()
        return

    def update_movie(self, movie: Movie, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        result.title = movie.title if movie.title is not None else result.title
        result.overview = movie.overview if movie.overview is not None else result.overview
        result.year = movie.year if movie.year is not None else result.year
        result.category = movie.category if movie.category is not None else result.category
        result.rating = movie.rating if movie.rating is not None else result.rating
        self.db.commit()
        return

    def delete_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        self.db.delete(result)
        self.db.commit()
        return result