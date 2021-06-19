def parse(ingredient):
    f = open("recipes.txt", "r")
    
    #ingredient = input("Enter an ingredient: ")
    # read contents line by line
    lines = f.readlines()
    
    count = 0
    for line in lines:
        if ingredient in line:
            count += 1
            print(count, "-", line, "\n")
    
    if count == 0:
        result = "Couldn't find " + ingredient + " in list"
    else:
        result ="Total " + str(count) + " results found"

    f.close()
    return result


def load_recipes():
    f = open("recipes.txt", "r")
    # read contents line by line
    lines = f.readlines()
    f.close()
    return lines

def save_recipe(text):
    return("OK")