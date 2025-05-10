from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine, get_db

from . import initial_setup
from . import routes
from .schemas import Ingredient, IngredientCreate, IngredientUpdate

app = FastAPI()


def create_tables():
    Base.metadata.create_all(bind=engine)


@app.on_event("startup")
async def startup_event():
    create_tables()


# --- INITIAL SETUP ---


@app.post("/init-db")
def init_db(db: Session = Depends(get_db)):
    return initial_setup.create_dummy_data(db)


@app.post("/delete-db")
def delete_db(db: Session = Depends(get_db)):
    return initial_setup.delete_all_dummy_data(db)


# --- INGREDIENTS ---


@app.post("/ingridients/", response_model=Ingredient)
def create_ingredient(ingredient: IngredientCreate, db: Session = Depends(get_db)):
    return routes.create_ingredient(db=db, ingredient=ingredient)


@app.get("/ingridients/{ingredient_id}", response_model=Ingredient)
def read_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    db_ingredient = routes.get_ingredient(db=db, ingredient_id=ingredient_id)
    if not db_ingredient:
        raise HTTPException(status_code=404, detail="Zutat nicht gefunden")
    return db_ingredient


@app.get("/ingridients/", response_model=list[Ingredient])
def read_ingredients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return routes.get_all_ingredients(db=db, skip=skip, limit=limit)


@app.put("/ingridients/{ingredient_id}", response_model=Ingredient)
def update_ingredient(
    ingredient_id: int, ingredient: IngredientUpdate, db: Session = Depends(get_db)
):
    updated_ingredient = routes.update_ingredient(
        db=db, ingredient_id=ingredient_id, ingredient=ingredient
    )
    if not updated_ingredient:
        raise HTTPException(status_code=404, detail="Zutat nicht gefunden")
    return updated_ingredient


@app.delete("/ingridients/{ingredient_id}", response_model=Ingredient)
def delete_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    deleted_ingredient = routes.delete_ingredient(db=db, ingredient_id=ingredient_id)
    if not deleted_ingredient:
        raise HTTPException(status_code=404, detail="Zutat nicht gefunden")
    return deleted_ingredient
