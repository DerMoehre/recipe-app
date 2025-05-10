from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models.models import Recipe, Ingredient, RecipeIngredient
from . import database_utils

app = FastAPI()


def create_tables():
    Base.metadata.create_all(bind=engine)


@app.on_event("startup")
async def startup_event():
    create_tables()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.post("/init-db")
def init_db(db: Session = Depends(get_db)):
    return database_utils.create_dummy_data(db)


@app.post("/delete-db")
def delete_db(db: Session = Depends(get_db)):
    return database_utils.delete_all_dummy_data(db)
