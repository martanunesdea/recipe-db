import tkinter as tk
from tkinter import ttk
import parser as parser
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RecipeDB")
        self.geometry("700x500")

        self.button_new_recipe = ttk.Button(self, text = "Add recipe", command = self.add_recipe)
        self.button_new_recipe.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.button_load_all = ttk.Button(self, text = "Load all recipes", command = self.load_recipes)
        self.button_load_all.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.button_look_up = ttk.Button(self, text = "Look up by word", command = self.lookup)
        self.button_look_up.grid(row = 0, column = 2, padx = 5, pady = 5)


    def new_window(self):
        newWindow = tk.Toplevel(self)
        newWindow.title("New Window")
        newWindow.geometry("800x800")
        return newWindow
    
    def add_recipe(self):
        newWindow = self.new_window()
        label = tk.Label(newWindow, text="Add recipe below")
        label.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.text_entry = tk.Text(newWindow, width = 70)
        self.text_entry.grid(row = 2, column = 0, columnspan = 4, padx = 5, pady = 5)

        submit = tk.Button(newWindow, text="Submit", command = self.db_save)
        submit.grid(row = 3, column = 0, padx = 5, pady = 5)
    
    def db_save(self):
        text = self.text_entry.get(1.0, tk.END)
        result = parser.save_recipe(text)
        print(result)

    def load_recipes(self):
        newWindow = self.new_window()
        text_entry = tk.Text(newWindow, width = 90)
        text_entry.grid(row=0, column=0)

        text = parser.load_recipes()
        text_entry.insert(1.0, text)

    def lookup(self):
        newWindow = self.new_window()    
        label = tk.Label(newWindow, text="Enter a keyword, ingredient, type of meal, etc.")
        label.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.text_entry = tk.Entry(newWindow)
        self.text_entry.grid(row = 2, column = 0, columnspan = 4, padx = 5, pady = 5)

        submit = tk.Button(newWindow, text="Submit",command = self.db_search)
        submit.grid(row = 3, column = 0, padx = 5, pady = 5)

        self.label1 = tk.StringVar()
        self.label1.set("")
        self.labelbar = tk.Label(newWindow, textvariable=self.label1)
        self.labelbar.grid(row=4, column = 0, padx = 5, pady = 5)

    def db_search(self):
        ingredient = self.text_entry.get()
        new_ingredient = ingredient.strip()
        print("Ingredient to look up:", new_ingredient)
        result = parser.parse(new_ingredient)
        self.label1.set(result)
        print(result)
        


