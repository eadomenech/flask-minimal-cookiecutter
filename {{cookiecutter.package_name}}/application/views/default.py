from flask import Blueprint, jsonify

default = Blueprint('default', __name__)


@default.route('/')
def index():
    return jsonify(**{'result': 'success'})
