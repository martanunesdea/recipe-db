## Script to find ingredients in recipes
def main():
    f = open("recipes.txt", "r")
    
    # read contents line by line
    lines = f.readlines()
    
    ingredient = input("Enter an ingredient: ")
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


if __name__ == "__main__": main()