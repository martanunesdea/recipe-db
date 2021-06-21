def get_database():
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    #CONNECTION_STRING = "mongodb+srv://cooluser:password123456789@<cluster-name>.mongodb.net/recipe-db"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = pymongo.MongoClient("mongodb+srv://cooluser:password12345@cluster0.sbchk.mongodb.net/recipe-db?retryWrites=true&w=majority")

    #db = client.test

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['recipe-db']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()
    
    collection_name = dbname["recipes"]
    item_1 = {
    "_id" : "U1IT00001",
    "item_name" : "recipe 3",
    }

    item_2 = {
    "_id" : "U1IT00002",
    "item_name" : "recipe 4",
    }
    
    collection_name.insert_many([item_1,item_2])
        
    item_details = collection_name.find()
    for item in item_details:
        # This does not give a very readable output
        print(item)