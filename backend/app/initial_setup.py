from sqlalchemy.orm import Session
from .database import Base, engine
from .models import Recipe, Ingredient, RecipeIngredient, Units, Tags, RecipeTag
from uuid import uuid4


def create_dummy_data(db: Session):
    # Einheiten erstellen
    unit_kopf = Units(name="Kopf")
    unit_mittel = Units(name="mittel")
    unit_g = Units(name="g")
    unit_ml = Units(name="ml")
    unit_el = Units(name="EL")
    unit_tl = Units(name="TL")
    unit_stueck = Units(name="Stück")
    unit_zehen = Units(name="Zehen")
    db.add_all([unit_kopf, unit_mittel, unit_g, unit_ml, unit_el, unit_tl, unit_stueck, unit_zehen])
    db.commit()
    db.refresh(unit_kopf)
    db.refresh(unit_mittel)
    db.refresh(unit_g)
    db.refresh(unit_ml)
    db.refresh(unit_el)
    db.refresh(unit_tl)
    db.refresh(unit_stueck)
    db.refresh(unit_zehen)

    # Tags erstellen
    tag_salat = Tags(name="Salat")
    tag_pasta = Tags(name="Pasta")
    tag_vegetarisch = Tags(name="vegetarisch")
    tag_einfach = Tags(name="einfach")
    tag_schnell = Tags(name="schnell")
    tag_italienisch = Tags(name="italienisch")
    tag_sauce = Tags(name="Sauce")
    db.add_all([tag_salat, tag_pasta, tag_vegetarisch, tag_einfach, tag_schnell, tag_italienisch, tag_sauce])
    db.commit()
    db.refresh(tag_salat)
    db.refresh(tag_pasta)
    db.refresh(tag_vegetarisch)
    db.refresh(tag_einfach)
    db.refresh(tag_schnell)
    db.refresh(tag_italienisch)
    db.refresh(tag_sauce)

    # Zutaten erstellen
    zutat1 = Ingredient(name="Salat")
    zutat2 = Ingredient(name="Tomaten")
    zutat3 = Ingredient(name="Zwiebeln")
    zutat4 = Ingredient(name="Nudeln")
    zutat5 = Ingredient(name="Knoblauch")
    db.add_all([zutat1, zutat2, zutat3, zutat4, zutat5])
    db.commit()
    db.refresh(zutat1)
    db.refresh(zutat2)
    db.refresh(zutat3)
    db.refresh(zutat4)
    db.refresh(zutat5)

    # Rezepte erstellen und mit Zutaten und Tags verknüpfen
    recipe1 = Recipe(
        name="Einfacher Salat",
        description="Ein schneller und gesunder Salat.",
        instructions="Alle Zutaten waschen und schneiden. Dressing mischen. Alles vermengen.",
        prep_time=10,
        cook_time=0,
        servings=2,
        tags=[tag_salat, tag_vegetarisch, tag_einfach, tag_schnell],
    )
    recipe2 = Recipe(
        name="Pasta mit Tomatensoße",
        description="Ein klassisches italienisches Gericht.",
        instructions="Pasta kochen. Zwiebeln und Knoblauch anbraten. Tomaten hinzufügen und köcheln lassen. Mit Pasta vermischen.",
        prep_time=15,
        cook_time=20,
        servings=4,
        tags=[tag_pasta, tag_vegetarisch, tag_italienisch, tag_sauce],
    )
    db.add_all([recipe1, recipe2])
    db.commit()
    db.refresh(recipe1)
    db.refresh(recipe2)

    # RecipeIngredient-Objekte erstellen (mit unit_id)
    rezept_zutat1_salat = RecipeIngredient(
        recipe_id=recipe1.id, ingredient_id=zutat1.id, quantity=1.0, unit_id=unit_kopf.id
    )
    rezept_zutat1_tomaten = RecipeIngredient(
        recipe_id=recipe1.id, ingredient_id=zutat2.id, quantity=2.0, unit_id=unit_mittel.id
    )
    rezept_zutat1_zwiebeln = RecipeIngredient(
        recipe_id=recipe1.id, ingredient_id=zutat3.id, quantity=0.5, unit_id=unit_mittel.id
    )
    rezept_zutat2_nudeln = RecipeIngredient(
        recipe_id=recipe2.id, ingredient_id=zutat4.id, quantity=500.0, unit_id=unit_g.id
    )
    rezept_zutat2_tomaten = RecipeIngredient(
        recipe_id=recipe2.id, ingredient_id=zutat2.id, quantity=400.0, unit_id=unit_g.id
    )
    rezept_zutat2_knoblauch = RecipeIngredient(
        recipe_id=recipe2.id, ingredient_id=zutat5.id, quantity=2.0, unit_id=unit_zehen.id
    )
    db.add_all([
        rezept_zutat1_salat,
        rezept_zutat1_tomaten,
        rezept_zutat1_zwiebeln,
        rezept_zutat2_nudeln,
        rezept_zutat2_tomaten,
        rezept_zutat2_knoblauch,
    ])
    db.commit()

    return {"message": "Dummy-Daten (mit Units und Tags) wurden hinzugefügt."}


def delete_all_dummy_data(db: Session):
    try:
        db.query(RecipeIngredient).delete()
        db.query(RecipeTag).delete()
        db.query(Recipe).delete()
        db.query(Ingredient).delete()
        db.query(Tags).delete()
        db.query(Units).delete()
        db.commit()
        return {"message": "Alle Dummy-Daten wurden gelöscht."}
    except Exception as e:
        db.rollback()
        raise e