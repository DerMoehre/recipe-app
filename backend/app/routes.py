from sqlalchemy.orm import Session
from .database import Base, engine
from . import models
from .schemas import Ingredient, IngredientCreate, IngredientUpdate
from fastapi import HTTPException


# --- INGREDIENTS ---
def get_ingredient(db: Session, ingredient_id: int):
    return (
        db.query(models.Ingredient)
        .filter(models.Ingredient.id == ingredient_id)
        .first()
    )


def get_all_ingredients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ingredient).offset(skip).limit(limit).all()


def create_ingredient(db: Session, ingredient: IngredientCreate):
    db_ingredient = (
        db.query(models.Ingredient)
        .filter(models.Ingredient.name == ingredient.name)
        .first()
    )
    if db_ingredient:
        raise HTTPException(
            status_code=400, detail="Zutat mit diesem Namen existiert bereits"
        )
    db_ingredient = models.Ingredient(name=ingredient.name)
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient


def update_ingredient(db: Session, ingredient_id: int, ingredient: IngredientUpdate):
    db_ingredient = (
        db.query(models.Ingredient)
        .filter(models.Ingredient.id == ingredient_id)
        .first()
    )
    if not db_ingredient:
        return None
    for key, value in ingredient.dict(exclude_unset=True).items():
        setattr(db_ingredient, key, value)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient


def delete_ingredient(db: Session, ingredient_id: int):
    db_ingredient = (
        db.query(models.Ingredient)
        .filter(models.Ingredient.id == ingredient_id)
        .first()
    )
    if not db_ingredient:
        return None
    db.delete(db_ingredient)
    db.commit()
    return db_ingredient
