from sqlalchemy.orm import Session
from .database import Base, engine
from .models import Recipe, Ingredient, RecipeIngredient, Unit, Tag, RecipeTag
from uuid import uuid4


def create_dummy_data(db: Session):
    # Einheiten erstellen
    unit_kopf = Unit(name="Kopf")
    unit_mittel = Unit(name="mittel")
    unit_g = Unit(name="g")
    unit_ml = Unit(name="ml")
    unit_el = Unit(name="EL")
    unit_tl = Unit(name="TL")
    unit_stueck = Unit(name="Stück")
    unit_zehen = Unit(name="Zehen")
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
    tag_salat = Tag(name="Salat")
    tag_pasta = Tag(name="Pasta")
    tag_vegetarisch = Tag(name="vegetarisch")
    tag_einfach = Tag(name="einfach")
    tag_schnell = Tag(name="schnell")
    tag_italienisch = Tag(name="italienisch")
    tag_sauce = Tag(name="Sauce")
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
        instructions=[
            "Salat waschen und in mundgerechte Stücke zupfen.",
            "Tomaten und Zwiebeln schneiden.",
            "Dressing nach Wahl zubereiten.",
            "Alle Zutaten in einer Schüssel vermengen und mit dem Dressing beträufeln.",
        ],
        calories=300,
        prep_time=10,
        cook_time=0,
        servings=2,
        tags=[tag_salat, tag_vegetarisch, tag_einfach, tag_schnell],
    )
    recipe2 = Recipe(
        name="Pasta mit Tomatensoße",
        description="Ein klassisches italienisches Gericht.",
        instructions=[
            "Wasser für die Pasta zum Kochen bringen und salzen.",
            "Pasta nach Packungsanweisung kochen.",
            "Für die Soße: Zwiebel schälen und würfeln.",
            "Knoblauch schälen und fein hacken.",
            "Zwiebel und Knoblauch in Olivenöl anbraten.",
            "Tomaten (passiert oder stückig) hinzufügen und köcheln lassen.",
            "Mit Salz, Pfeffer und italienischen Kräutern würzen.",
            "Gekochte Pasta abgießen und zur Soße geben. Gut vermischen.",
        ],
        sauce_instructions= ["Für die Tomatensoße: Zwiebeln und Knoblauch anbraten.", 
                             "Tomaten hinzufügen und köcheln lassen.",
                             "Mit Salz, Pfeffer und Kräutern würzen."
        ],
        calories=None,
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
        db.query(Tag).delete()
        db.query(Unit).delete()
        db.commit()
        return {"message": "Alle Dummy-Daten wurden gelöscht."}
    except Exception as e:
        db.rollback()
        raise e