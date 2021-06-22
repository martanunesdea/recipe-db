from .gui import *
from .db import *

def main():
    app = Application()
    app.mainloop()

    item_1 = {
    "name" : "risotto",
    "tags": "vegeterian"
    } 
    item_2 = {
    "name" : "bolognese",
    "tags" : "beef"
    } 
    #new_items = compile_items(item_1, item_2)
    #insert_items(new_items)
   
    #get_item_by_name("risotto")

    
if __name__ == "__main__": main()

