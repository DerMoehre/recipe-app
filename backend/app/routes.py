from sqlalchemy.orm import Session
from .database import Base, engine
from . import models
from .schemas import (
    Ingredient, 
    IngredientCreate, 
    IngredientUpdate,
    Unit,
    UnitCreate,
    UnitUpdate
)
from fastapi import HTTPException


# --- INGREDIENTS ---
def get_ingredient(db: Session, ingredient_id: str):
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


def update_ingredient(db: Session, ingredient_id: str, ingredient: IngredientUpdate):
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


def delete_ingredient(db: Session, ingredient_id: str):
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

# --- UNITS ---
def get_unit(db: Session, unit_id: str):
    return (
        db.query(models.Unit)
        .filter(models.Unit.id == unit_id)
        .first()
    )

def get_all_units(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Unit).offset(skip).limit(limit).all()


def create_unit(db: Session, unit: UnitCreate):
    db_unit = (
        db.query(models.Unit)
        .filter(models.Unit.name == unit.name)
        .first()
    )
    if db_unit:
        raise HTTPException(
            status_code=400, detail="Einheit mit diesem Namen existiert bereits"
        )
    db_unit = models.Unit(name=unit.name)
    db.add(db_unit)
    db.commit()
    db.refresh(db_unit)
    return db_unit


def update_unit(db: Session, unit_id: str, unit: UnitUpdate):
    db_unit = (
        db.query(models.Unit)
        .filter(models.Unit.id == unit_id)
        .first()
    )
    if not db_unit:
        return None
    for key, value in unit.dict(exclude_unset=True).items():
        setattr(db_unit, key, value)
    db.commit()
    db.refresh(db_unit)
    return db_unit


def delete_unit(db: Session, unit_id: str):
    db_unit = (
        db.query(models.Unit)
        .filter(models.Unit.id == unit_id)
        .first()
    )
    if not db_unit:
        return None
    db.delete(db_unit)
    db.commit()
    return db_unit