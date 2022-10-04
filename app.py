#!flask/bin/python
from flask import Flask, jsonify
import json


app = Flask(__name__)

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



# JSON file
f = open ('pokemon.json', "r")

# Reading from file
tasks = json.loads(f.read())


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/pokemon/api/v1.0/pokemon_id/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    return task[0]



@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
