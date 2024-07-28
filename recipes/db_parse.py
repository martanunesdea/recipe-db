import os
def parse_text(filename):
    # Parse the text file
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in file:
            print(line)

    # Extract title, ingredients, and instructions
    title = lines[0].strip()
    start_index = lines.index('Ingredients\n') + 1
    end_index = lines.index('Instructions\n')
    ingredients = ''.join(lines[start_index:end_index]).strip()
    instructions = ''.join(lines[end_index + 1:]).strip()
    
    return [title, ingredients, instructions]


def save_insert_query_to_file(table_name, column_names, input_names, file_path):
    # Construct the parameterized insert query
    placeholders = ", ".join([f'"{i}"' for i in input_names])
    insert_query = f'INSERT INTO {table_name} ({", ".join(column_names)}) VALUES ({placeholders});\n'

    # Write the insert query to the file
    with open(file_path, 'a') as file:
        file.write(insert_query)
        file.write("\n\n")


def read_file_lines(file_path):
    ingredients = []
    ingredients_section = False
    with open(file_path, 'r') as file:
        for line in file:
            print(line)


# Example usage:

table_name = 'recipes'
column_names = ['title', 'ingredients', 'instructions']
file_path = 'test_schema.sql'


txt_files = []
directory_path = "./"
count = 0
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):
        print(count+1, "recipe: ", filename)
        input_names = parse_text(filename)
        save_insert_query_to_file(table_name, column_names, input_names, file_path)
        count+=1

print("Finished writing to sql file.")