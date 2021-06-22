from .db import db_get_all, db_lookup_name, db_insert

def find_recipes(ingredient):
    result = db_lookup_name(ingredient)
    return result


def load_recipes():
    result = db_get_all()
    return result

def save_recipe(title, ingredients, method, tags):
    ingr_list = ingredients.splitlines()
    method_list = method.splitlines()
    tags_list = tags.splitlines()
    entry = {
        "name": title,
        "ingredients": ingr_list,
        "method": method_list,
        "tags": tags_list
    }
    print(entry)
    db_insert(entry)

    
    