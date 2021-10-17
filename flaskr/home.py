from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
from .recipe import recipe_get_titles, recipe_add, recipe_full_details
from .recipe import recipe_delete, recipe_update, recipe_lookup_id, recipe_search
bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    recipes = recipe_get_titles()
    return render_template('recipes/index.html', recipes=recipes)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        error = recipe_add(request.form)
        if error is None:
            return redirect(url_for('home.index'))
        else:
            flash(error)

    return render_template('recipes/create.html')

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    recipe = recipe_lookup_id(id)

    if request.method == 'POST':
        error = recipe_update(id, request.form)
        if error is None:
            return redirect(url_for('home.view_full_details', id=id))
        else:
            flash(error)
    
    return render_template('recipes/update.html', post=recipe)

@bp.route('/<int:id>/view_full_details', methods=('GET',))
def view_full_details(id):
    title, ingredients, instructions = recipe_full_details(id)
    return render_template('recipes/view_full_details.html', title=title, ingredients=ingredients, instructions=instructions)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    error = recipe_delete(id)
    if error is None:
        return redirect(url_for('home.index'))
    else: 
        flash(error)
        return redirect(url_for('home.view_full_details', id=id))

@bp.route('/search/<string:query>', methods=('GET', 'POST',))
def search(query):
    term = request.args.get("q")
    recipes = recipe_search(term)

    return render_template('recipes/search_results.html', recipes=recipes)
