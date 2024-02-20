from models.movie_model import MovieModel
from fastapi import HTTPException

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

    def create_movies(self, movie):
        new_movie = MovieModel(**movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()

    def update_movie(self, movie, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        if not result:
            raise HTTPException(status_code=404, content={"Message": 'Movie not found'})
        else:
            result.title = movie.title if movie.title is not None else result.title
            result.overview = movie.overview if movie.overview is not None else result.overview
            result.year = movie.year if movie.year is not None else result.year
            result.category = movie.category if movie.category is not None else result.category
            result.rating = movie.rating if movie.rating is not None else result.rating
            self.db.commit()

    def delete_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result