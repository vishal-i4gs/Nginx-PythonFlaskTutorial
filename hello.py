import uuid
import base64

from flask import Flask, request, jsonify, json
from flask_uuid import FlaskUUID
from jose import jwt

app = Flask(__name__)
flask_uuid = FlaskUUID()
flask_uuid.init_app(app)

todoItems = []

@app.route("/")
def hello() :
	return "Welcome to TodoList!"

@app.route("/service/create_todo", methods=["POST"])
def create_todo() :
	print request.headers
	todoItem = {
	"id" : uuid.uuid4(),
	"title" : request.json["title"],
	"description" : request.json["description"],
	"importance" : request.json["importance"],
	"completed" : False
	}
	print todoItem

	# print request.headers["authorization"]

	auth = request.headers["authorization"]
	header = jwt.get_unverified_header(auth)

	access_token = request.headers["access-token"]
	print request.headers["access-token"]

	# payload = jwt.decode("eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik1VUTNOamcyTkRnd05EQTVNVGMzUkVGRk5EaEJPRGN6TWpoRE56SkJRams1TVRnME9EQkRSZyJ9.eyJpc3MiOiJodHRwczovL2p1c3R2aXNoLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1OTlmZTNmZWRkY2MxYjM2OTc1NmRkNTUiLCJhdWQiOiJXTkRwa0JPVTFVRzVGS1pBTmNESm5MakpscDd4Vk91MiIsImlhdCI6MTUwMzY1MTAwMSwiZXhwIjoxNTAzNjg3MDAxfQ.UlYx5QDEGrVmW8krZcPvIG5KMexWRGCVVWCR-MmKwMbXqDhsLdEf36bIWV-7wrlzgO9qOogMn-Bz43m5K_Oy8iCpcPnzW9TxHD8MW6x-DDxnZTaqxW9EHM6gpu2gJnzCOmgiYMPRjoRg7xwWGzeyJxG8tjJg4dXTiaSUaCx25bPM4lPFGpu1EgyycCRJnN-ZH12syt5Uq7vOYsdDqgzfE9nqK30dfI7isEWjUc5ursYpz6x0HhxdEmlIJjSxeQJg13NGErn8XLRBA3hEoiA2stiBTJ6kJv0Vy-LrAUsGUtagC-i0gp71Cw5CgG9o0FMFXsNVZN-fa0kScFPuHJNZcA",'rdavG_bA8qMdB5c_fvLazvWJa3zdHrYw6U_0so8zpGJoqMGwtrfnRbIC1hdIJszW',['HS256'])

	jwks = {"keys":[{"alg":"RS256","kty":"RSA","use":"sig","x5c":["MIIC/zCCAeegAwIBAgIJFUo+2ASfagkiMA0GCSqGSIb3DQEBCwUAMB0xGzAZBgNVBAMTEmp1c3R2aXNoLmF1dGgwLmNvbTAeFw0xNzA2MDEwNzM2NDdaFw0zMTAyMDgwNzM2NDdaMB0xGzAZBgNVBAMTEmp1c3R2aXNoLmF1dGgwLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAP/wvD73Ef1f6XpwWKanVdFbxRSv4PGo6/cDsVCUbHuvsl8MR9GRAQRX1fcdkwzfikKer07rsANbHL9qAcX0tQcG8TeJ146a0UHZUFI6M35SuIKmSjggYAJGI0/psOw17E0pwPxX3sk1WyhfXzYymf2B2jzLWNGV7U4hgAPYWCijAsKdfUKWeUdZEfBrK2nqYrQCxhsu5ygChYfLxPUJmyPDp3BSiCpW7yygjXeaHDxWlTw4b2joc+fXYJnHVMAFhiTT2vhGpX8CO7xRYvXx3rO8Z0akpKN3FQvVsUdIpJoBRfuTeNBinkLFAhsqvI3CIjUuGdUDx1JvHHsDlLWm2IsCAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUKRKPx5ojcaGYDm+qxR6AV52O6XMwDgYDVR0PAQH/BAQDAgKEMA0GCSqGSIb3DQEBCwUAA4IBAQAtB5kxsC0Z0Fs14ET+m5T0k6VMvUpz7e80J/m0avyu9Wh5aL2BgDX0BlrAZF6k96U8cVPCf/2wX5vf18jZk1VpMoRPRqcjXdC2akkeJAplDTrHoYRRSSBm/Y8wtv7SrcWJCeUTWMcIwerxnKS79IahDVJ0Z06I3rXsV2yDDvMmCdXi3b9aBftleWr5RRJ/uTKzVhhXiqs0iDgb5jktuqsjbVegyNru/prn7ZmIyzN/xVInF5I+MsvIxyXkOpybRzvkZqG58L2YhIgPxy8BE0XvOox4cHoO3RrvvYyOZxbE6bZuhabwYVH+F11LVqzH4yEQBDaQll284R3Qe3mrr28c"],"n":"__C8PvcR_V_penBYpqdV0VvFFK_g8ajr9wOxUJRse6-yXwxH0ZEBBFfV9x2TDN-KQp6vTuuwA1scv2oBxfS1BwbxN4nXjprRQdlQUjozflK4gqZKOCBgAkYjT-mw7DXsTSnA_FfeyTVbKF9fNjKZ_YHaPMtY0ZXtTiGAA9hYKKMCwp19QpZ5R1kR8GsraepitALGGy7nKAKFh8vE9QmbI8OncFKIKlbvLKCNd5ocPFaVPDhvaOhz59dgmcdUwAWGJNPa-EalfwI7vFFi9fHes7xnRqSko3cVC9WxR0ikmgFF-5N40GKeQsUCGyq8jcIiNS4Z1QPHUm8cewOUtabYiw","e":"AQAB","kid":"MUQ3Njg2NDgwNDA5MTc3REFFNDhBODczMjhDNzJBQjk5MTg0ODBDRg","x5t":"MUQ3Njg2NDgwNDA5MTc3REFFNDhBODczMjhDNzJBQjk5MTg0ODBDRg"}]}

        for key in jwks["keys"]:
                        secret = {
                                "kty": key["kty"],
                                "kid": key["kid"],
                                "use": key["use"],
                                "n": key["n"],
                                "e": key["e"]
                        }

    	# secret = 'rdavG_bA8qMdB5c_fvLazvWJa3zdHrYw6U_0so8zpGJoqMGwtrfnRbIC1hdIJszW'
    	# secret = base64.b64decode(secret, '-_')

			print "auth is "+auth
			payload =jwt.decode(auth, secret,['RS256'],audience="WNDpkBOU1UG5FKZANcDJnLjJlp7xVOu2",access_token=access_token)
			print payload

	# print payload
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
