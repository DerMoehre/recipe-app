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
    id: int

    class Config:
        orm_mode = True


# RecipeIngredient Schemas
class RecipeIngredientBase(BaseModel):
    quantity: float
    unit: str


class RecipeIngredientCreate(RecipeIngredientBase):
    recipe_id: int
    ingredient_id: int


class RecipeIngredientUpdate(RecipeIngredientBase):
    pass


class RecipeIngredient(RecipeIngredientBase):
    recipe_id: int
    ingredient_id: int

    class Config:
        orm_mode = True


# Recipe Schemas
class RecipeBase(BaseModel):
    name: str
    description: Optional[str] = None
    instructions: str
    prep_time: Optional[int] = None
    cook_time: Optional[int] = None
    servings: Optional[int] = None


class RecipeCreate(RecipeBase):
    pass


class RecipeUpdate(RecipeBase):
    pass


class Recipe(RecipeBase):
    id: int
    created_at: datetime
    updated_at: datetime
    ingredients: List[Ingredient] = []

    class Config:
        orm_mode = True
