import tkinter as tk
from tkinter import ttk
from .parser import find_recipes, load_recipes, save_recipe

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
        title_label = tk.Label(newWindow, text="Add recipe name:")
        title_label.pack()
        self.title_entry = tk.Entry(newWindow, width = 50)
        self.title_entry.pack()
        ingredients_label = tk.Label(newWindow, text="Add ingredients (one per line):")
        ingredients_label.pack()
        self.ingredients_entry = tk.Text(newWindow, width = 90, height = 12)
        self.ingredients_entry.pack()
        method_label = tk.Label(newWindow, text="Add instructions (one line per instruction):")
        method_label.pack()
        self.method_entry = tk.Text(newWindow, width = 90, height = 20)
        self.method_entry.pack()
        tags_label = tk.Label(newWindow, text="Add tags (one line per tag):")
        tags_label.pack()
        self.tags_entry = tk.Text(newWindow, width = 90, height = 5)
        self.tags_entry.pack()

        submit = tk.Button(newWindow, text="Submit", command = self.save)
        submit.pack()
    
    def save(self):
        title = self.title_entry.get()
        ingredients = self.ingredients_entry.get(1.0, tk.END)
        method = self.method_entry.get(1.0, tk.END)
        tags = self.tags_entry.get(1.0, tk.END)
        save_recipe(title, ingredients, method, tags)

    def load_recipes(self):
        newWindow = self.new_window()
        text_entry = tk.Text(newWindow, width = 120)
        text_entry.pack()

        text = load_recipes()
        text_entry.insert(1.0, text)

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
        result = find_recipes(new_ingredient)
        self.label1.set(result)
        


