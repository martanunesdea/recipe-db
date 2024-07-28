def read_file_lines(file_path):
    ingredients = []
    ingredients_section = False
    with open(file_path, 'r') as file:
        for line in file:
            if "Ingredients" in line:
                ingredients_section = True
            if "Instructions" in line:
                ingredients_section = False
                instructions_section = True
            if ingredients_section and not "Ingredients" in line:
                # Remove leading and trailing whitespace from each line
                cleaned_line = line.strip()
                ingredients.append(cleaned_line)
        
    with open(file_path, 'r') as file:
        text = file.read()
        phrases = list()
        instructions = list ()
        # Split the text into phrases using dot as delimiter
        for line in text.split('.'):
            if line.startswith('\n'):
                line = line.replace('\n', '')
            if (line.startswith('\n') == False) and ('\n' in line):
                line = line.replace('\n', '.')
            phrases.append(line)
        phrases = [line.split('.') for line in phrases]
        print(phrases)
        # Find the index of the target word in the list of strings
        for index, string in enumerate(phrases):
                if "Instructions" in string:
                    # Return a new list containing strings from the target word onwards
                    instructions = phrases[index+1:]
    
        print(instructions)
        


    return ingredients


# Example usage:
file_path = 'persian_lentils.txt'  # Replace with the path to your text file
lines = read_file_lines(file_path)
print(lines)