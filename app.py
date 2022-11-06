from flask import Flask, jsonify

app = Flask( __name__ )

from data import todos

@app.route("/")
def root():
    return("<h1>Hola mundo</h1>")

@app.route("/todos")
def getTodos():
    return jsonify(todos)

@app.route("/todos/<string:id_todo>")
def getTodo(id_todo):
    todo = [todo for todo in todos if todo['id'] == id_todo]
    return todo

if __name__ == '__main__':
    app.run( debug = True, port = 4000 )