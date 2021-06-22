from .db import db_get_all

def parse(ingredient):
    f = open("recipes.txt", "r")
    
    #ingredient = input("Enter an ingredient: ")
    # read contents line by line
    lines = f.readlines()
    
    count = 0
    result = ""
    for line in lines:
        if ingredient in line:
            count += 1
            result1 = str(count) + " - " + line + "\n"
            result = result + result1
    
    if count == 0:
        result = "Couldn't find " + ingredient + " in list"
    
    f.close()
    return result


def load_recipes():
    result = db_get_all()
    """
    f = open("recipes.txt", "r")
    # read contents line by line
    lines = f.readlines()
    f.close()
    """
    return result

def save_recipe(text):
    return("OK")