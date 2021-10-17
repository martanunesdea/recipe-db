
# FastAPI's jsonable_encoder handles converting various non-JSON types,
# such as datetime between JSON types and native Python types.
from fastapi.encoders import jsonable_encoder
# Pydantic, and Python's built-in typing are used to define a schema
# that defines the structure and types of the different objects stored
# in the recipes collection, and managed by this API.
from typing import List
from flaskr.db import db_get_recipes, db_lookup_name, insert_recipe, db_lookup_id, db_delete, db_update

class Recipe():
    id: int
    name: str
    ingredients: List[str]

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data.get("_id") is None:
            data.pop("_id", None)
        return data

def recipe_lookup_id(id):
    unformatted_recipe = db_lookup_id(id)
    this_tags = ""
    for field in unformatted_recipe:
        for k, val in field.items():
            if k == "id":
                this_id = val
            if k == "name" or k == "title":
                this_name = val
            if k == "ingredients":
                this_ingredients = val
            if k == "instructions":
                this_instructions = val
            if k == "tags":
                this_tags = val
        entry = {"id": this_id, "title": this_name, "ingredients": this_ingredients, "instructions": this_instructions, "tags": this_tags}
    return entry

def recipe_get_titles():
    recipes = db_get_recipes()
    recipe_list = list()
    id = str()
    recipe_title = str()
    for recipe in recipes:
        for k, val in recipe.items():
            if k == "id":
                id = val
            if k == "name" or k == "title":
                recipe_title = val
        recipe_list.append({"id": id, "title": recipe_title})
    return recipe_list
    
def recipe_add(form):
    title = form['title']
    ingredients = form['ingredients']
    instructions = form['instructions']
   
    if not title or not ingredients or not instructions:
        return('Missing required information.')
    
    recipe = {'title': title, 'ingredients': ingredients, 'instructions': instructions}
    insert_recipe(recipe)
    return

def recipe_full_details(id):
    recipe = recipe_lookup_id(id)
    title = recipe["title"]
    ingredients = recipe["ingredients"]
    instructions = recipe["instructions"]
     
    return title, ingredients, instructions

def recipe_update(id, form):
    title = form['title']
    ingredients = form['ingredients']
    instructions = form['instructions']
    if not title:
            return('Title is required.')
    else:
        db_update(id, title, ingredients, instructions)
    return

def recipe_delete(id):
    if db_delete(id):
        return
    else:
        return "Could not delete"

def recipe_lookup_name(name):
    recipes = db_lookup_name(name)
    text = ""
    for entry in recipes:
        for k, val in entry.items():
            if k == "_id":
                pass
            if k == "name":
                line = f'\nTitle: {val}\n'
                text = text + line
            if k == "ingredients":
                line = f'Ingredients:\n'
                text = text + line
                for ing in val:
                    line = f'{ing}\n'
                    text = text + line
            if k == "instructions":
                line = f'Instructions:\n'
                text = text + line
                for inst in val:
                    line = f'{inst}\n'
                    text = text + line
            if k == "tags":
                line = f'Categories: {val}\n'
                text = text + line
        
    return text

def recipe_search(terms):
    unformatted_recipe = db_lookup_name(terms)
    print(unformatted_recipe)
    this_ingredients = ""
    this_instructions = ""
    this_tags = ""

    for field in unformatted_recipe:
        for k, val in field.items():
            if k == "id":
                this_id = val
            if k == "name" or k == "title":
                this_name = val
                print(this_name)
            if k == "ingredients":
                this_ingredients = val
            if k == "instructions":
                this_instructions = val
            if k == "tags":
                this_tags = val
        entry = [{"id": this_id, "title": this_name, "ingredients": this_ingredients, "instructions": this_instructions, "tags": this_tags}]
    return entry