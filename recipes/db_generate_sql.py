def parse_text(file_path):
    # Parse the text file
    with open(file_path, 'r') as file:
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



input_names = parse_text("butternut_squash_sage_risotto.txt")
# Example usage:
table_name = 'recipes'
column_names = ['title', 'ingredients', 'instructions']
file_path = 'new_test_schema.sql'

save_insert_query_to_file(table_name, column_names, input_names, file_path)
