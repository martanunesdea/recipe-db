def parse(ingredient):
    f = open("recipes.txt", "r")
    
    # read contents line by line
    lines = f.readlines()
    
    count = 0
    for line in lines:
        if ingredient in line:
            count += 1
            print(count, "-", line, "\n")
    
    if count == 0:
        print("Couldn't find", ingredient,"in list")
    else:
        print("Total", count, "results found")


    f.close()


def load_recipes():
    f = open("recipes.txt", "r")
    # read contents line by line
    lines = f.readlines()
    print(lines)
    f.close()
    return lines

def save_recipe(text):
    return("OK")