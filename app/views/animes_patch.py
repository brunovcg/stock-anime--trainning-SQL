from flask import Blueprint, request
from app.services import patch_one, check_post_or_patch_entries, get_specific_id

bp_animes = Blueprint('animes_patch', __name__, url_prefix='/')

# Em vez de @app, utilizamos a instancia de blueprint criada, bp_hello
@bp_animes.patch('/animes/<int:anime_id>')
def update(anime_id):

    data = request.get_json()

    if 'anime' in data:
        data['anime'] = data["anime"].title()
   

    entries_are_not_ok = check_post_or_patch_entries(data)

    test_table_exist = get_specific_id(anime_id)

    if test_table_exist  == "table doesn't exist" or test_table_exist == []:
        return {'error' : 'Not Found'}, 404

    if entries_are_not_ok:
        return entries_are_not_ok, 422

    result = patch_one(anime_id, data)

    if result == 'Not Found':
        return {'error' : 'Not Found'}, 404


    return result, 200