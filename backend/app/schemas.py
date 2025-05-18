from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# Ingredient Schemas
class IngredientBase(BaseModel):
    name: str


class IngredientCreate(IngredientBase):
    pass


class IngredientUpdate(IngredientBase):
    pass


class Ingredient(IngredientBase):
    id: str

    class Config:
        orm_mode = True

# Unit Schemas
class UnitBase(BaseModel):
    name: str

class UnitCreate(UnitBase):
    pass

class UnitUpdate(UnitBase):
    pass

class Unit(UnitBase):
    id: int

    class Config:
        orm_mode = True

# Tag Schemas
class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class TagUpdate(TagBase):
    pass

class Tag(TagBase):
    id: str

    class Config:
        orm_mode = True

# RecipeIngredient Schemas
class RecipeIngredientBase(BaseModel):
    quantity: float
    unit: str


class RecipeIngredientCreate(RecipeIngredientBase):
    recipe_id: str
    ingredient_id: str


class RecipeIngredientUpdate(RecipeIngredientBase):
    pass


class RecipeIngredient(RecipeIngredientBase):
    recipe_id: str
    ingredient_id: str
    unit_id: str
    unit: Optional[Unit] = None

    class Config:
        orm_mode = True


# Recipe Schemas
class RecipeBase(BaseModel):
    name: str
    description: Optional[str] = None
    instructions: List[str]
    sauce_instructions: List[str] = []
    prep_time: Optional[int] = None
    cook_time: Optional[int] = None
    servings: Optional[int] = None
    tags: List[Tag] = []


class RecipeCreate(RecipeBase):
    tags: List[str] = []


class RecipeUpdate(RecipeBase):
    tags: List[str] = []


class Recipe(RecipeBase):
    id: str
    created_at: datetime
    updated_at: datetime
    ingredients: List[Ingredient] = []
    tags: List[Tag] = []

    class Config:
        orm_mode = True
