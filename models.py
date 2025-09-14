from pydantic import BaseModel, Field 

class Book(BaseModel):

    title : str = Field(...,min_length=1, max_length=100,description="Title of the book")
    author : str = Field(...,min_length=1, max_length=50,description="Author of the book")
    year : int = Field(...,ge=1000,le=2024,description="Publication year of the book")
    isbn : str = Field(...,min_length=10, max_length=13,description="ISBN number of the book")

