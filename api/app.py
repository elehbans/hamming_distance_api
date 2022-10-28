### DEPENDENCIES ###
import sqlite3
from flask import request, abort, jsonify, Blueprint, Flask, render_template
from werkzeug.exceptions import BadRequest

from api.config import Config
from api.db import init_db
from api.utils.get_sequences import get_sequences
from api.utils.data_management import parse_sample_data, insert_sample_data

blueprint = Blueprint('hamming_distance_api', __name__)

def get_db_connection():
    conn = sqlite3.connect(Config.DATABASE_NAME)
    return conn

### ERROR HANDLING ###
@blueprint.errorhandler(404)
def resource_not_found(e):
    return jsonify(error='Invalid Route'), 404

@blueprint.errorhandler(403)
def prohibited_request_type(e):
    return jsonify(error='Prohibited Request Type'), 403

@blueprint.errorhandler(400)
def bad_request(e: BadRequest):
    return e


### ENDPOINTS ###
@blueprint.route('/hamming_distance', methods = ['GET'])
def contacts():
    if request.method == 'GET':
        args = request.args
        sequence = args.get('sequence')
        
        if sequence is not None:
            conn = get_db_connection()
            results = get_sequences(conn=conn, target_sequence=sequence)
            return results.to_json(orient='records'), 200
        else:
            abort(400)
    else:
        abort(403)

### INDEX ###
@blueprint.route('/', methods = ['GET'])
def index_form():
    return render_template('index.html')

def create_app(mode="testing"):
    app = Flask(__name__) 
    app.config.from_object(Config)
    app.register_blueprint(blueprint) 

    if mode == 'testing':
        with app.app_context():
            conn = init_db(app)
            ####
            # TODO: create upload functionality and remove this
            data = parse_sample_data()
            insert_sample_data(data = data, conn = conn) 
            ####
            conn.close()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()


    