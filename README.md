# Recipe DB 
This repository aims to create a user interface to browse through a collection of recipes. The advantage it brings is to find recipes not only by their name, but also by ingredients or text contained within the recipe (e.g. style of cooking, dinner or lunch recipes, number of servings, etc.). 

The user requirements for this digital recipe cookbook may change over time, but the scope of this project will include:


- Keeping a collection of recipes, visible to anyone.
- Authentication system, to register and login users who may want to create or add their recipes.
- To create a recipe, a user must register and login.
- To create a recipe, it must have a **title**, a set of **ingredients**, and a set of **instructions**. Otherwise, the creation of the recipe is not successful.
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


## MongodDB structure
MongoDB is used as the database solution, because it provides more flexibility when it comes to storing varying amounts of text for the "ingredients" and "instructions. 
The Mongo database instance was generated on Mongo Atlas, and two collections were created: "users" and "recipes".
- "users" collection: Designed to store the email, username and password hashes. 
- "recipes" collection: Design to store the details of the recipes. Currently, it doesn't store the author id or author name, although this could be implemented in the future.

## How to run the project
Dependencies for the project:
- Python
- Flask
- PyMongo
- MongoDB Collection - this is running on a cloud instance. It will go dormant after extended periods of being unused. Will need to log in and activate the collection if that's the case.

On the terminal run "flask run". 