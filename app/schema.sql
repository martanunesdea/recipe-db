DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS ingredients;
DROP TABLE IF EXISTS users;

CREATE TABLE recipes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  ingredients TEXT NOT NULL,
  instructions TEXT NOT NULL
);

CREATE TABLE ingredients (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name INTEGER NOT NULL
);


CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  password TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL
);

INSERT INTO recipes (title, ingredients, instructions) 
VALUES ('testname', 'testingredients', 'testinstructions');


INSERT INTO recipes (title, ingredients, instructions) 
VALUES ('test2', 'ingre2', 'instr2');


INSERT INTO recipes (title, ingredients, instructions) 
VALUES ('testname', 'testingredients', 'testinstructions');
