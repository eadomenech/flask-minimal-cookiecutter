from flask import current_app, Blueprint, jsonify

default = Blueprint('default', __name__)

@default.route('/')
def index():
    return jsonify(**{'result': 'success'})
