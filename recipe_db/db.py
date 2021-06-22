import pymongo

def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://cooluser:password12345@cluster0.sbchk.mongodb.net/recipe-db?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = pymongo.MongoClient(CONNECTION_STRING)

    return client['recipe-db']
    
def compile_items(*args):
    items = []
    for item in args:
        items.append(item)
        print(item)
    return items

def insert_items(items):
    dbname = get_database()
    collection_name = dbname["recipes"]
    collection_name.insert_many(items)
    
def db_get_all():
    dbname = get_database()
    
    collection_name = dbname["recipes"]
   
    recipes = collection_name.find()
    text = ""
    for recipe in recipes:
        for k, val in recipe.items():
            if k == "_id":
                pass
            if k == "name":
                line = f'\nTitle: {val}\n'
                text = text + line
            if k == "ingredients":
                line = f'Ingredients:\n'
                text = text + line
                for ing in val:
                    line = f'\t{ing}\n'
                    text = text + line
            if k == "tags":
                line = f'Categories: {val}\n'
                text = text + line
    return text
   

def db_lookup_name(in_name):
    dbname = get_database()
    
    collection_name = dbname["recipes"]

    recipes = collection_name.find( { "name": in_name } )
    text = ""
    for entry in recipes:
        for k, val in entry.items():
            if k == "_id":
                pass
            if k == "name":
                line = f'\nTitle: {val}\n'
                text = text + line
            if k == "ingredients":
                line = f'Ingredients:\n'
                text = text + line
                for ing in val:
                    line = f'{ing}\n'
                    text = text + line
            if k == "tags":
                line = f'Categories: {val}\n'
                text = text + line
    return text
