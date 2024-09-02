"""
Dieses Modul enthält Funktionen zur Anpassung von Rezepten basierend auf der Anzahl der Portionen
und zum Laden von Rezepten aus JSON-Strings.
"""

import json


def adjust_recipe(recipe_dict, new_servings):
    """
    Passt die Zutatenmengen eines Rezepts basierend auf der neuen Anzahl an Personen an.

    :param recipe_dict: Ein Dictionary, das das Rezept beschreibt
    :param new_servings: Die neue Anzahl an Personen
    :return: Ein neues Dictionary mit angepassten Zutatenmengen
    """
    # Berechne den Anpassungsfaktor zur Anpassung der Mengen
    servings_factor = new_servings / recipe_dict['servings']

    # Erstelle ein neues Rezept-Dictionary mit angepassten Mengen
    adjusted_recipe = {
        'title': recipe_dict['title'],
        'ingredients': {
            ingredient: amount * servings_factor
            for ingredient, amount in recipe_dict['ingredients'].items()
        },
        'servings': new_servings
    }

    return adjusted_recipe


def load_recipe(json_string):
    """
    Wandelt einen JSON-String in ein Python-Dictionary um.

    :param json_string: JSON-kodierter String, der das Rezept beschreibt
    :return: Ein Dictionary, das das Rezept beschreibt
    """
    return json.loads(json_string)


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json_string = (
        '{"title": "Spaghetti Bolognese", '
        '"ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, '
        '"servings": 4}'
    )

    # Lade das Rezept aus dem JSON-String
    recipe_data = load_recipe(recipe_json_string)

    # Gebe die neue Anzahl an Personen an
    new_servings_count = 2

    # Passe das Rezept an die neue Anzahl an Personen an
    updated_recipe = adjust_recipe(recipe_data, new_servings_count)

    # Ausgabe der Ergebnisse
    print('Original Recipe:')
    print(recipe_data)

    print('\nAdjusted Recipe:')
    print(updated_recipe)
    # new comment for commit
