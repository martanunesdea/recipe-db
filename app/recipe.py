from app.db import db_get_recipes, db_lookup, db_insert_recipe, db_delete, db_update, db_text_search

# Utilities
def parse(recipe):
    this_id = ""
    this_name = ""
    this_ingredients = ""
    this_instructions = ""
    this_tags = ""
    entry = dict()
    for k, val in recipe.items():
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

def format_recipes(cursor, single):
    if single == True:
        for recipe in cursor:
            result = parse(recipe)
    else:
        result = list()
        for recipe in cursor:
            result.append(parse(recipe))
    
    return result

def recipe_lookup_id(id):
    raw_recipe = db_lookup("id", id)
    return format_recipes(raw_recipe, single=True)

# CRUD operations
def recipe_get_all():
    recipes = db_get_recipes()
    recipe_list = format_recipes(recipes, single=False)
    return recipe_list
    
def recipe_get_one(id):
    recipe = recipe_lookup_id(id)
    title = recipe["title"]
    ingredients = recipe["ingredients"]
    instructions = recipe["instructions"]
    # Prepare for display
    ingredients = ingredients.split('\n')
    instructions = instructions.split('\n')

    return title, ingredients, instructions

def recipe_add(form):
    title = form['title']
    ingredients = form['ingredients']
    instructions = form['instructions']
   
    if not title or not ingredients or not instructions:
        return('Missing required information.')
    
    recipe = {'title': title, 'ingredients': ingredients, 'instructions': instructions}
    db_insert_recipe(recipe)
    return

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

# Text search
def recipe_search(terms):
    recipes = db_text_search(terms)
    if len(recipes) < 0:
        res = 0
    else:
        res = format_recipes(recipes, single=False)

    print(res)
    return res


