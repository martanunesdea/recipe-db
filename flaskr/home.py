from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    db = get_db()
    recipes = db.execute(
        'SELECT p.id, title, ingredients, instructions, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
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
            db = get_db()
            db.execute(
                'INSERT INTO post (title, ingredients, instructions, author_id)'
                ' VALUES (?, ?, ?, ?)',
                (title, ingredients, instructions, g.user['id'])
            )
            db.commit()
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
@login_required
def view_full_details(id):
    recipe = get_post(id)
    title = recipe["title"]
    ingredients = recipe["ingredients"]
    instructions = recipe["instructions"]

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
    print(term)
    recipes = db.execute('SELECT * FROM post where title = ?', (term,)).fetchall()
    db.commit()
    #get_post(id)
    #db = get_db()
    #db.execute('DELETE FROM post WHERE id = ?', (id,))
    #db.commit()
    return render_template('recipes/search_results.html', recipes=recipes)