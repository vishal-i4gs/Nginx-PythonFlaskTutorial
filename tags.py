import uuid
import time

from flask import Flask, request, jsonify, json
from flask_uuid import FlaskUUID

app = Flask(__name__)
flask_uuid = FlaskUUID()
flask_uuid.init_app(app)

tags = []

@app.route("/service/tags/dropped", methods=["PUT"])
def put_tags_dropped() :
	print request.data
	tagId = request.data
	try:
		val = uuid.UUID(tagId)
	except ValueError:
		return "Bad request",403,{'Content-Type':"text/html"}
	tag = {
		"id" : uuid.UUID(tagId),
		"droppedTime" : int(time.time())
		}
	print tag
	tags.append(tag)
	return "Success",200,{'Content-Type':"text/html"}

@app.route("/service/tags/dropped", methods=["GET"])
def get_tags_dropped():
  	return json.dumps(tags), 200, {'Content-Type': "application/json"}

if __name__ == "__main__":
      app.run()
