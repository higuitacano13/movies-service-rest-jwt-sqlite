from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime


class Movie(BaseModel): 
    id: Optional[int] = None
    title: str = Field(min_length=1, max_length=100)
    overview: str = Field(min_length=15, max_length=150)
    year: int
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=1, max_length=15)

    @validator('year')
    def validate_year(cls, v):
        current_year = datetime.now().year
        if v > current_year:
            raise ValueError(f"El año no puede ser mayor que el año actual ({current_year})")
        return v

    class Config:
        json_schema_extra = {
            "example":{
                "id": 1,
                "title": "Título película",
                "overview": "Descripción",
                "year": 1990,
                "rating": 1.0,
                "category": "Acción"
            }
        }