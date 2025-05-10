from sqlalchemy.orm import Session
from .database import Base, engine
from .models.models import Recipe, Ingredient, RecipeIngredient


def create_tables():
    Base.metadata.create_all(bind=engine)


def create_dummy_data(db: Session):
    zutat1 = Ingredient(name="Salat")
    zutat2 = Ingredient(name="Tomaten")
    zutat3 = Ingredient(name="Zwiebeln")
    zutat4 = Ingredient(name="Nudeln")
    zutat5 = Ingredient(name="Knoblauch")

    recipe1 = Recipe(
        name="Einfacher Salat",
        description="Ein schneller und gesunder Salat.",
        instructions="Alle Zutaten waschen und schneiden. Dressing mischen. Alles vermengen.",
        prep_time=10,
        cook_time=0,
        servings=2,
    )
    recipe2 = Recipe(
        name="Pasta mit Tomatensoße",
        description="Ein klassisches italienisches Gericht.",
        instructions="Pasta kochen. Zwiebeln und Knoblauch anbraten. Tomaten hinzufügen und köcheln lassen. Mit Pasta vermischen.",
        prep_time=15,
        cook_time=20,
        servings=4,
    )
    rezept_zutat1_salat = RecipeIngredient(
        recipe=recipe1, ingredient=zutat1, quantity=1, unit="Kopf"
    )
    rezept_zutat1_tomaten = RecipeIngredient(
        recipe=recipe1, ingredient=zutat2, quantity=2, unit="mittel"
    )
    rezept_zutat1_zwiebeln = RecipeIngredient(
        recipe=recipe1, ingredient=zutat3, quantity=0.5, unit="mittel"
    )

    rezept_zutat2_nudeln = RecipeIngredient(
        recipe=recipe2, ingredient=zutat4, quantity=500, unit="g"
    )
    rezept_zutat2_tomaten = RecipeIngredient(
        recipe=recipe2, ingredient=zutat2, quantity=400, unit="g"
    )
    rezept_zutat2_knoblauch = RecipeIngredient(
        recipe=recipe2, ingredient=zutat5, quantity=2, unit="Zehen"
    )

    db.add_all(
        [
            zutat1,
            zutat2,
            zutat3,
            zutat4,
            zutat5,
            recipe1,
            recipe2,
            rezept_zutat1_salat,
            rezept_zutat1_tomaten,
            rezept_zutat1_zwiebeln,
            rezept_zutat2_nudeln,
            rezept_zutat2_tomaten,
            rezept_zutat2_knoblauch,
        ]
    )
    db.commit()
    return {"message": "Dummy-Daten wurden hinzugefügt."}


def delete_all_dummy_data(db: Session):
    try:
        db.query(RecipeIngredient).delete()
        db.query(Recipe).delete()
        db.query(Ingredient).delete()
        db.commit()
        return {"message": "Alle Dummy-Daten wurden gelöscht."}
    except Exception as e:
        db.rollback()
        raise e
