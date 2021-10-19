import os
from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flask import jsonify 

import json

app = Flask(__name__)
# app = Flask(__name__, template_folder='./templates')
api = Api(app)

@app.route("/", methods=['GET'])
def sensor_api():
	# x = { "name": "John", "age": 30, "city": "New York" }
	# convert into JSON:
	# y = json.dumps(x)

	return jsonify({"status": "ok"})


host = 'http://localhost'
port = '8000'
if __name__ == '__main__':
	#app.run(debug=True)
	app.run(debug=True, host='0.0.0.0', port=port)