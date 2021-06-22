import tkinter as tk
from tkinter import ttk
from .parser import parse, load_recipes, save_recipe

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RecipeDB")
        self.geometry("200x120")

        self.button_new_recipe = ttk.Button(self, text = "Add recipe", command = self.add_recipe)
        self.button_new_recipe.pack()

        self.button_load_all = ttk.Button(self, text = "Load all recipes", command = self.load_recipes)
        self.button_load_all.pack()

        self.button_look_up = ttk.Button(self, text = "Look up by word", command = self.lookup)
        self.button_look_up.pack()

    def new_window(self):
        newWindow = tk.Toplevel(self)
        newWindow.title("New Window")
        newWindow.geometry("800x800")
        return newWindow
    
    def add_recipe(self):
        newWindow = self.new_window()
        label = tk.Label(newWindow, text="Add recipe below")
        label.pack()
        self.text_entry = tk.Text(newWindow, width = 70)
        self.text_entry.pack()

        submit = tk.Button(newWindow, text="Submit", command = self.db_save)
        submit.pack()
    
    def db_save(self):
        text = self.text_entry.get(1.0, tk.END)
        result = save_recipe(text)
        print(result)

    def load_recipes(self):
        newWindow = self.new_window()
        text_entry = tk.Text(newWindow, width = 120)
        text_entry.pack()

        text = load_recipes()
        loc = 1.0
        for entry in text:
            for k, val in entry.items():
                if k != "_id" and k != "ingredients":
                    line = f'{k}: {val}\n'
                    text_entry.insert(loc, line)
                    loc = loc + 100
                if k == "ingredients":
                    for ing in val:
                        line = f'\t{ing}\n'
                        text_entry.insert(loc, line)
                        loc += 100
                

        #text_entry.insert(1.0, text)

    def lookup(self):
        newWindow = self.new_window()    
        label = tk.Label(newWindow, text="Enter a keyword, ingredient, type of meal, etc.")
        label.pack()
        self.text_entry = tk.Entry(newWindow)
        self.text_entry.pack()

        submit = tk.Button(newWindow, text="Submit",command = self.db_search)
        submit.pack()

        self.label1 = tk.StringVar()
        self.label1.set("")
        self.labelbar = tk.Label(newWindow, textvariable=self.label1)
        self.labelbar.pack()

    def db_search(self):
        ingredient = self.text_entry.get()
        new_ingredient = ingredient.strip()
        print("Ingredient to look up:", new_ingredient)
        result = parse(new_ingredient)
        self.label1.set(result)
        print(result)
        


