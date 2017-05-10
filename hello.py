import uuid

from flask import Flask, request, jsonify, json
from flask_uuid import FlaskUUID

app = Flask(__name__)
flask_uuid = FlaskUUID()
flask_uuid.init_app(app)

todoItems = []

@app.route("/")
def hello() :
	return "Welcome to TodoList!"

@app.route("/service/create_todo", methods=["POST"])
def create_todo() :
	print request.data
	todoItem = {
	"id" : uuid.uuid4(),
	"title" : request.json["title"],
	"description" : request.json["description"],
	"importance" : request.json["importance"],
	"completed" : False
	}
	print todoItem
	todoItems.append(todoItem)
	return "TodoItemAdded",200,{'Content-Type':"text/html"}
	#content = request.data
	#fo = open("test.txt","a")
    	#fo.write(content)
	#print content
	#return request.data

@app.route("/service/show_todos", methods=["GET"])
def show_todos():
  	return json.dumps(todoItems), 200, {'Content-Type': "application/json"}
	#  return jsonify({todoItems})

@app.route('/service/todo/<uuid:id>')
def showTodo(id):
	todoItem = filter(lambda t: t['id'] == id, todoItems)
        return jsonify(todoItem[0])

@app.route('/service/todo/<uuid:id>/complete')
def completeTodo(id):
	todoItem = filter(lambda t: t["id"] == id, todoItems)
	todoItem[0]["completed"] = True
	print todoItem[0]
	return jsonify(todoItem[0])

if __name__ == "__main__":
	app.run()
