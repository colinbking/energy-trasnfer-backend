from flask import Flask, jsonify
from process import mainstuff
from flask_cors import CORS
from energyChallenge import readfile
import json


main = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]
CORS(main)


@main.route('/', methods=['GET'])
def index():
    mapping, l = readfile()
    answer = mainstuff(mapping, l)
    return jsonify(answer)

if __name__ == '__main__':
    main.run(debug=True)