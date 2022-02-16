from flask import Flask, render_template, request, jsonify
from pusher import Pusher
import json

# create flask app
app = Flask(__name__)

# configure pusher object
pusher = Pusher(
    app_id='app_id',
    key='my_key',
    secret='my_secret',
    cluster='my_cluster',
    ssl=True
)

# endpoint for storing todo item
@app.route('/add-todo', methods = ['POST'])
def addTodo():
    data = "Some random text"
    pusher.trigger('todo', 'item-added', data) # trigger `item-added` event on `todo` channel
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)