def parse_recipe(text):
    lines = text.split('\n')
    ingredients = []
    instructions = []
    is_ingredients_section = False
    is_instructions_section = False

    for line in lines:
        line = line.strip()
        if line == "Ingredients":
            is_ingredients_section = True
            is_instructions_section = False
        elif line == "Instructions":
            is_ingredients_section = False
            is_instructions_section = True
        elif is_ingredients_section:
            ingredients.append(line)
        elif is_instructions_section:
            instructions.append(line)

    return ingredients, instructions

file_path = 'persian_lentils.txt'
with open(file_path, 'r') as file:
    input_text = file.read()
ingredients, instructions = parse_recipe(input_text)

print("Ingredients:")
for ingredient in ingredients:
    print(ingredient)

print("\nInstructions:")
for step, instruction in enumerate(instructions, start=1):
    print(f"{step}. {instruction}")