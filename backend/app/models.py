import uuid

from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.types import PickleType
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(Text)
    instructions = Column(PickleType, nullable=False)
    sauce_instructions = Column(PickleType)
    prep_time = Column(Integer)
    cook_time = Column(Integer)
    servings = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    recipe_ingredients = relationship(
        "RecipeIngredient", back_populates="recipe", cascade="all, delete-orphan"
    )
    ingredients = relationship(
        "Ingredient",
        secondary="recipe_ingredients",
        back_populates="recipes",
        overlaps="recipe_ingredients",
    )

    tags = relationship("Tag", secondary="recipe_tags", back_populates="recipes")
    recipe_tags = relationship("RecipeTag", back_populates="recipe")

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, unique=True, nullable=False)

    recipe_ingredients = relationship(
        "RecipeIngredient", back_populates="ingredient", cascade="all, delete-orphan"
    )
    recipes = relationship(
        "Recipe",
        secondary="recipe_ingredients",
        back_populates="ingredients",
        overlaps="recipe_ingredients",
    )

class Tag(Base):
    __tablename__ = "tags"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, unique=True, nullable=False)

    recipes = relationship("Recipe", secondary="recipe_tags", back_populates="tags")
    recipe_tags = relationship("RecipeTag", back_populates="tag")

class Unit(Base):
    __tablename__ = "units"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, unique=True, nullable=False)

    recipe_ingredients = relationship(
        "RecipeIngredient", back_populates="unit", cascade="all, delete-orphan"
    )

class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    recipe_id = Column(String(36), ForeignKey("recipes.id"), primary_key=True)
    ingredient_id = Column(String(36), ForeignKey("ingredients.id"), primary_key=True)
    unit_id = Column(String(36), ForeignKey("units.id"))
    quantity = Column(Float)

    unit = relationship(
        "Unit", back_populates="recipe_ingredients", overlaps="ingredients,recipes"
    )
    recipe = relationship(
        "Recipe", back_populates="recipe_ingredients", overlaps="ingredients,recipes"
    )
    ingredient = relationship(
        "Ingredient",
        back_populates="recipe_ingredients",
        overlaps="ingredients,recipes",
    )

class RecipeTag(Base):
    __tablename__ = "recipe_tags"

    recipe_id = Column(String(36), ForeignKey("recipes.id"), primary_key=True)
    tag_id = Column(String(36), ForeignKey("tags.id"), primary_key=True)

    recipe = relationship("Recipe", back_populates="recipe_tags")
    tag = relationship("Tag", back_populates="recipe_tags")

