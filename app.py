from flask import Flask, jsonify, request
import sys
import bson.json_util as json_util
from flask_restful import Api, Resource
from bson import ObjectId
import json
import subprocess
from models import trends_collection
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(JSONEncoder, self).default(obj)

app.json_encoder = JSONEncoder

class TrendListResource(Resource):
    def get(self):
        # Fetch data from MongoDB
        trends = list(trends_collection.find())
        # Convert MongoDB documents to JSON-compatible format
        return jsonify(json.loads(json_util.dumps(trends)))

    def post(self):
        data = request.get_json()
        trends_collection.insert_one(data)
        return {'message': 'Trend added'}, 201

class AnalysisResultsResource(Resource):
    def get(self):
        # Fetch and return the analysis results from wherever they are stored
        # This is an example path; adjust according to your storage
        results = {"example": "data"}  # Replace with actual data retrieval
        return jsonify(results)

class DataOperationsResource(Resource):
    def get(self):
        python_executable = sys.executable  # Get the path to the Python executable in the virtual environment
        try:
            result = subprocess.run([python_executable, "data_cleaning.py"], check=True, capture_output=True, text=True)
            print(result.stdout)  # Log standard output
            print(result.stderr)  # Log standard error

            result = subprocess.run([python_executable, "data_analysis.py"], check=True, capture_output=True, text=True)
            print(result.stdout)  # Log standard output
            print(result.stderr)  # Log standard error

            return {'message': 'Data operations completed'}, 200
        except subprocess.CalledProcessError as e:
            # Capture and log the error details
            return {'error': str(e), 'stdout': e.stdout, 'stderr': e.stderr}, 500


api.add_resource(TrendListResource, '/api/trends')
api.add_resource(AnalysisResultsResource, '/api/analysis-results')
api.add_resource(DataOperationsResource, '/api/data-operations')

@app.route('/')
def home():
    return 'Hello, Flask!'
@app.route('/api/python-path')
def get_python_path():
    return jsonify({'python_path': sys.executable})
if __name__ == '__main__':
    app.run(debug=True)
