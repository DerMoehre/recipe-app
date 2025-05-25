from sqlalchemy.orm import Session, selectinload
from .database import Base, engine
from . import models
from .schemas import (
    Ingredient, 
    IngredientCreate, 
    IngredientUpdate,
    Unit,
    UnitCreate,
    UnitUpdate,
    Tag,
    TagCreate,
    TagUpdate,
    Recipe,
    RecipeCreate
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

def get_ingredient_by_name(db: Session, name: str):
    return db.query(models.Ingredient).filter(models.Ingredient.name == name).first()

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

def get_unit_by_name(db: Session, name: str):
    return db.query(models.Unit).filter(models.Unit.name == name).first()

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


# --- TAGS ---
def get_tag(db: Session, tag_id: str):
    return (
        db.query(models.Tag)
        .filter(models.Tag.id == tag_id)
        .first()
    )

def get_all_tags(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tag).offset(skip).limit(limit).all()

def get_tag_by_name(db: Session, name: str):
    return db.query(models.Tag).filter(models.Tag.name == name).first()

def create_tag(db: Session, tag: TagCreate):
    db_tag = (
        db.query(models.Tag)
        .filter(models.Tag.name == tag.name)
        .first()
    )
    if db_tag:
        raise HTTPException(
            status_code=400, detail="Tag mit diesem Namen existiert bereits"
        )
    db_tag = models.Tag(name=tag.name)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def update_tag(db: Session, tag_id: str, tag: TagUpdate):
    db_tag = (
        db.query(models.Tag)
        .filter(models.Tag.id == tag_id)
        .first()
    )
    if not db_tag:
        return None
    for key, value in tag.dict(exclude_unset=True).items():
        setattr(db_tag, key, value)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def delete_tag(db: Session, tag_id: str):
    db_tag = (
        db.query(models.Tag)
        .filter(models.Tag.id == tag_id)
        .first()
    )
    if not db_tag:
        return None
    db.delete(db_tag)
    db.commit()
    return db_tag


# --- RECIPE ---#
def get_recipe(db:Session, recipe_id: str):
    return (
        db.query(models.Recipe)
        .options(
            selectinload(models.Recipe.recipe_ingredients).selectinload(models.RecipeIngredient.ingredient),
            selectinload(models.Recipe.recipe_ingredients).selectinload(models.RecipeIngredient.unit),
            selectinload(models.Recipe.tags)
        )
        .filter(models.Recipe.id == recipe_id)
        .first()
    )

def get_all_recipes(db:Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Recipe)
        .options(
            selectinload(models.Recipe.recipe_ingredients).selectinload(models.RecipeIngredient.ingredient),
            selectinload(models.Recipe.recipe_ingredients).selectinload(models.RecipeIngredient.unit),
            selectinload(models.Recipe.tags)
        )
        .offset(skip)
        .limit(limit)
        .all()
    )

def create_recipe(db: Session, recipe: RecipeCreate):
    db_recipe = (
        db.query(models.Recipe)
        .filter(models.Recipe.name == recipe.name)
        .first()
    )
    if db_recipe:
        raise HTTPException(
            status_code=400, detail="Rezept mit diesem Namen existiert bereits"
        )
    db_recipe = models.Recipe(
        name=recipe.name,
        description=recipe.description,
        instructions=recipe.instructions,
        sauce_instructions=recipe.sauce_instructions,
        calories=recipe.calories,
        prep_time=recipe.prep_time,
        cook_time=recipe.cook_time,
        servings=recipe.servings,
    )
    db.add(db_recipe)
    db.flush()

    if recipe.tags:
        for tag_name in recipe.tags:
            db_tag = get_tag_by_name(db, name=tag_name)
            if not db_tag:
                db_tag = create_tag(db, tag=TagCreate(name=tag_name))

            db_recipe_tag = models.RecipeTag(
                recipe_id=db_recipe.id,
                tag_id=db_tag.id
            )
            db.add(db_recipe_tag)

    if recipe.ingredients:
        for ri_data in recipe.ingredients:
            db_ingredient = get_ingredient_by_name(db, name=ri_data.ingredient_name)
            if not db_ingredient:
                db_ingredient =create_ingredient(db, ingredient=IngredientCreate(name=ri_data.ingredient_name))

            db_unit = None
            if ri_data.unit_name:
                db_unit = get_unit_by_name(db, name=ri_data.unit_name)
                if not db_unit:
                    db_unit = create_unit(db, unit=UnitCreate(name=ri_data.unit_name))

            db_recipe_ingredient = models.RecipeIngredient(
                recipe_id=db_recipe.id,
                ingredient_id=db_ingredient.id,
                quantity=ri_data.quantity,
                unit_id=db_unit.id if db_unit else None
            )
            db.add(db_recipe_ingredient)

    db.commit()
    db.refresh(db_recipe)
    return get_recipe(db, recipe_id=db_recipe.id)