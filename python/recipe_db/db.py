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
    
def get_all_items():
    dbname = get_database()
    
    collection_name = dbname["recipes"]
   
    item_details = collection_name.find()
    for item in item_details:
        # This does not give a very readable output
        print(item)

# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":  
    item_1 = {
    "name" : "risotto",
    "tags": "vegeterian"
    } 
    item_2 = {
    "name" : "bolognese",
    "tags" : "beef"
    } 
    items = compile_items(item_1, item_2)
    insert_items(items)
    get_all_items()