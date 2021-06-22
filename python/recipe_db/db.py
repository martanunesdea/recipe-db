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
   
    item_details = collection_name.find()
    #items = []
    
    
    return item_details

def get_item_by_name(in_name):
    dbname = get_database()
    
    collection_name = dbname["recipes"]

    res = collection_name.find( { "name": in_name } )
    for x in res:
        for k, val in x.items():
            if k != "_id":
                print(k, " ", val)
        
