# Recipe DB 
This repository aims to create an interface that allows an user to browse through recipes and find recipes by the ingredients contained within them.

The user requirements for this digital recipe cookbook may change over time, but the scope of this project will include:


- Keeping a collection of recipes, visible to anyone.
- To create a recipe, a user must register and login.
- To create a recipe, it must have a **title**, a set of **ingredients**, and a set of **instructions**. Otherwise, the creation of the recipe is not successful.
- Upon creation, the user may view the full details of the recipe.
- Upon creation, the author may edit the contents of the recipe.
- Search recipe by name
- Search recipe by ingredient
- Regex search.

New points to build on:
- Recipe recommendation system
- Have a "favourite" recipes page
- Have a "reduce waste" recommendation system

## Stack
The project is run with Flask as the back-end server and MongoDB as the database engine.

## Project structure
The main app is inside the folder "Flaskr". It contains
- "static" folder: For css and js files
- "templates" folder: For html files
     - base.html: Base HTML template used in the other templates
     - "auth" folder: HTML files for the authentication pages
     - "recipes" folder: HTML files for the recipe interface pages
- __init__.py - starting point for the app
- auth.py - blueprint responsible for authentication routes
- home.py - blueprint responsible for the recipe-interface routes
- recipe.py - middleware that interacts with db.py for DB tasks
- user.py - middleware that interacts with db.py for authentication DB tasks
- db.py - file responsible of managing the DB interactions

The "tests" folder contains the tests.
The "config.py" file in the main directory contains the different configurations used for development and testing.
