from app.db import db_get_recipes, db_lookup, db_insert_recipe, db_delete, db_update, db_text_search

# Utilities
def parse(recipe):
    recipe_fields = ['id', 'title', 'ingredients', 'instructions', 'tags']
    recipe = dict(zip(recipe_fields, recipe))
    return recipe

def format_recipes(cursor, single):
    if single == True:
        result = parse(cursor)
    else:
        result = list()
        for item in cursor:       
            recipe = parse(item)
            result.append((recipe))

    return result

def recipe_lookup_id(id):
    raw_recipe = db_lookup("recipes", "id", id)
    return format_recipes(raw_recipe, single=True)

# CRUD operations
def recipe_get_all():
    recipes = db_get_recipes()
    recipe_list = format_recipes(recipes, single=False)
    return recipe_list

def recipe_get_popular_tags():
    tags = ['vegetarian', 'lunch', 'chicken', 'fish', 'italian', 'asian', 'mexican']
    return tags
    
def recipe_get_one(id):
    recipe = recipe_lookup_id(id)
    title = recipe["title"]
    ingredients = recipe["ingredients"]
    instructions = recipe["instructions"]
    tags = recipe["tags"]
    # Prepare for display
    ingredients = ingredients.split('\n')
    instructions = instructions.split('\n')
    tags = tags.split('\n')


    return title, ingredients, instructions, tags

def recipe_add(form):
    title = form['title']
    ingredients = form['ingredients']
    instructions = form['instructions']
    tags = form['tags']
   
    if not title or not ingredients or not instructions:
        return('Missing required information.')
    
    recipe = {'title': title, 'ingredients': ingredients, 'instructions': instructions, 'tags': tags}
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
def recipe_search(terms, by_tag=False):
    if by_tag == True:
        recipes = db_text_search(terms)
    else:
        recipes = db_text_search(terms)
    
    if isinstance(recipes, list):
        res = format_recipes(recipes, single=False)
    else:
        res = format_recipes(recipes, single=True)

    return res


