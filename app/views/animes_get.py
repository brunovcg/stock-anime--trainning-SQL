from flask import Blueprint
from app.services import get_all

bp_animes = Blueprint('animes_get', __name__, url_prefix='/')

# Em vez de @app, utilizamos a instancia de blueprint criada, bp_hello
@bp_animes.get('/animes')
def get_create():

    result = get_all()

    if result == "table doesn't exist":
        return {'data' : []}, 200

    return {'data' : result }, 200