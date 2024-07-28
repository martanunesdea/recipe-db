from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.auth import login_required
from .recipe import recipe_get_all, recipe_add, recipe_get_one
from .recipe import recipe_delete, recipe_update, recipe_lookup_id, recipe_search, recipe_get_popular_tags
bp = Blueprint('home', __name__)
from app.forms import PostForm

@bp.route('/')
def index():
    recipes = recipe_get_all()
    tags = recipe_get_popular_tags()
    return render_template('recipes/index.html', recipes=recipes, filter_words=tags)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    form = PostForm()

    if form.validate_on_submit():
        error = recipe_add(form.data)
        if error is None:
            flash('Your post is now live!')
            return redirect(url_for('home.index'))
        else:
            flash(error)
    
    return render_template('recipes/create.html', form=form)


@bp.route('/filter_recipes/<string:filter>')
def filter_recipes(filter):
    if filter == "reset":
        recipes = recipe_get_all()
    else:
        recipes = recipe_search(filter, by_tag=True)
    
    tags = recipe_get_popular_tags()
    return render_template('recipes/index.html', recipes=recipes, filter_words=tags)


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
    title, ingredients, instructions, tags = recipe_get_one(id)
    if tags is None:
        tags = []
    return render_template('recipes/view_full_details.html', id=id, title=title, ingredients=ingredients, instructions=instructions, tags=tags)


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
    tags = recipe_get_popular_tags()
    return render_template('recipes/index.html', recipes=recipes, filter_words=tags)
