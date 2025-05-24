from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine, get_db

from . import initial_setup
from . import routes
from .schemas import (
    Ingredient, 
    IngredientCreate, 
    IngredientUpdate,
    Unit,
    UnitCreate,
    UnitUpdate,
    Tag,
    TagCreate,
    TagUpdate
)

app = FastAPI()


def create_tables():
    Base.metadata.create_all(bind=engine)


@app.on_event("startup")
async def startup_event():
    create_tables()


# --- INITIAL SETUP ---
@app.post("/init-db", tags=["Initial Setup"])
def init_db(db: Session = Depends(get_db)):
    return initial_setup.create_dummy_data(db)


@app.post("/delete-db", tags=["Initial Setup"])
def delete_db(db: Session = Depends(get_db)):
    return initial_setup.delete_all_dummy_data(db)


# --- INGREDIENTS ---
@app.post("/ingridients/", response_model=Ingredient, tags=["Ingredients"])
def create_ingredient(ingredient: IngredientCreate, db: Session = Depends(get_db)):
    return routes.create_ingredient(db=db, ingredient=ingredient)


@app.get("/ingridients/{ingredient_id}", response_model=Ingredient, tags=["Ingredients"])
def read_ingredient(ingredient_id: str, db: Session = Depends(get_db)):
    db_ingredient = routes.get_ingredient(db=db, ingredient_id=ingredient_id)
    if not db_ingredient:
        raise HTTPException(status_code=404, detail="Zutat nicht gefunden")
    return db_ingredient


@app.get("/ingridients/", response_model=list[Ingredient], tags=["Ingredients"])
def read_ingredients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return routes.get_all_ingredients(db=db, skip=skip, limit=limit)


@app.put("/ingridients/{ingredient_id}", response_model=Ingredient, tags=["Ingredients"])
def update_ingredient(
    ingredient_id: str, ingredient: IngredientUpdate, db: Session = Depends(get_db)
):
    updated_ingredient = routes.update_ingredient(
        db=db, ingredient_id=ingredient_id, ingredient=ingredient
    )
    if not updated_ingredient:
        raise HTTPException(status_code=404, detail="Zutat nicht gefunden")
    return updated_ingredient


@app.delete("/ingridients/{ingredient_id}", response_model=Ingredient, tags=["Ingredients"])
def delete_ingredient(ingredient_id: str, db: Session = Depends(get_db)):
    deleted_ingredient = routes.delete_ingredient(db=db, ingredient_id=ingredient_id)
    if not deleted_ingredient:
        raise HTTPException(status_code=404, detail="Zutat nicht gefunden")
    return deleted_ingredient

# --- UNITS ---
@app.post("/units/", response_model=Unit, tags=["Units"])
def create_unit(unit: UnitCreate, db: Session = Depends(get_db)):
    return routes.create_unit(db=db, unit=unit)


@app.get("/units/{unit_id}", response_model=Unit, tags=["Units"])
def read_unit(unit_id: str, db: Session = Depends(get_db)):
    db_unit = routes.get_unit(db=db, unit_id=unit_id)
    if not db_unit:
        raise HTTPException(status_code=404, detail="Einheit nicht gefunden")
    return db_unit


@app.get("/units/", response_model=list[Unit], tags=["Units"])
def read_units(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return routes.get_all_units(db=db, skip=skip, limit=limit)


@app.put("/units/{unit_id}", response_model=Unit, tags=["Units"])
def update_unit(
    unit_id: str, unit: UnitUpdate, db: Session = Depends(get_db)
):
    updated_unit = routes.update_unit(
        db=db, unit_id=unit_id, unit=unit
    )
    if not updated_unit:
        raise HTTPException(status_code=404, detail="Einheit nicht gefunden")
    return updated_unit


@app.delete("/units/{unit_id}", response_model=Unit, tags=["Units"])
def delete_unit(unit_id: str, db: Session = Depends(get_db)):
    deleted_unit = routes.delete_unit(db=db, unit_id=unit_id)
    if not deleted_unit:
        raise HTTPException(status_code=404, detail="Einheit nicht gefunden")
    return deleted_unit

# --- TAGS ---
@app.post("/tags/", response_model=Tag, tags=["Tags"])
def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
    return routes.create_tag(db=db, tag=tag)


@app.get("/tags/{tag_id}", response_model=Tag, tags=["Tags"])
def read_tag(tag_id: str, db: Session = Depends(get_db)):
    db_tag = routes.get_tag(db=db, tag_id=tag_id)
    if not db_tag:
        raise HTTPException(status_code=404, detail="Tag nicht gefunden")
    return db_tag


@app.get("/tags/", response_model=list[Tag], tags=["Tags"])
def read_tags(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return routes.get_all_tags(db=db, skip=skip, limit=limit)

@app.put("/tags/{tag_id}", response_model=Tag, tags=["Tags"])
def update_tag(
    tag_id: str, tag: TagUpdate, db: Session = Depends(get_db)
):
    updated_tag = routes.update_tag(
        db=db, tag_id=tag_id, tag=tag
    )
    if not updated_tag:
        raise HTTPException(status_code=404, detail="Tag nicht gefunden")
    return updated_tag


@app.delete("/tags/{tag_id}", response_model=Tag, tags=["Tags"])
def delete_tag(tag_id: str, db: Session = Depends(get_db)):
    deleted_tag = routes.delete_tag(db=db, tag_id=tag_id)
    if not deleted_tag:
        raise HTTPException(status_code=404, detail="Tag nicht gefunden")
    return deleted_tag