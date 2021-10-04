from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db, db_get_recipes, db_lookup_id
import flaskr.db as db

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    recipes = db_get_recipes()
    #for recipe in recipes:
        #print(recipe)
    
    return render_template('recipes/index.html', posts=recipes)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            recipe = {'title': title, 'ingredients': ingredients, 'instructions': instructions}
            db.insert_recipe(recipe)
            return redirect(url_for('home.index'))

    return render_template('recipes/create.html')

def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, ingredients, instructions, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    recipe = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute('UPDATE post SET title = ?, ingredients = ?, instructions = ?'
            'WHERE id = ?', (title, ingredients, instructions, id))
            db.commit()
            return redirect(url_for('home.index'))

    return render_template('recipes/update.html', post=recipe)

@bp.route('/<int:id>/view_full_details', methods=('GET',))
def view_full_details(id):
    recipe = db_lookup_id(id)
    title = recipe["title"]
    ingredients = recipe["ingredients"]
    #instructions = recipe["instructions"]
    instructions = "instructions here"
    return render_template('recipes/view_full_details.html', title=title, ingredients=ingredients, instructions=instructions)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('home.index'))


@bp.route('/search/<string:query>', methods=('GET', 'POST',))
def search(query):
    term = request.args.get("q")
    db = get_db()
    recipes = db.execute('SELECT * FROM post where title = ?', (term,)).fetchall()
    db.commit()
    
    return render_template('recipes/search_results.html', recipes=recipes)