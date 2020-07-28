from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import json
import logging
import os

# Init Flask and DB variables.
api = Flask(__name__)
# api.config['SECRET_KEY'] = os.environ.get("SECRETKEY")
# api.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DBLOCATION")
api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_env.db'
api.config['JSON_SORT_KEYS'] = False
api.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# api.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 10, 'pool_recycle': 120, 'pool_pre_ping': True, 'pool_timeout': 3}
db = SQLAlchemy(api)
os.makedirs(os.path.dirname('../log/apipostlog.txt'), exist_ok=True)
logging.basicConfig(filename='../log/apipostlog.log', level=logging.ERROR)

from models import Job
import crud

# POST route for saving new Job Posting. Body must be in JSON format
@api.route('/api/job', methods=['POST'])
def job_post_route():
    if request.method == 'POST': # Checks current requested method.
        try:
            receivedjson = request.get_json() # Parse body sent as JSON
            jobdata = Job(receivedjson["name"], receivedjson["company"], receivedjson["description"], receivedjson["location"], receivedjson["contract"], receivedjson["tags"], receivedjson["new"], receivedjson["featured"], datetime.now(), False)
            db.session.add(jobdata) # jobdata variable created from Job object above added to 
            db.session.commit() # Commit to database for persistance
            return jsonify({"status": 201}), 201
        except Exception as exp:
            logging.exception("Exception:" + str(exp))
            return jsonify({"status": 404}), 404

# GET route for getting all jobs saved in database.
@api.route('/api/jobs', methods=['GET'])
def jobs_get_route():
    if request.method == 'GET': # Checks current requested method.
        try:
            return jsonify(crud.get_jobs()), 200
        except Exception as exp:
            logging.exception("Exception:" + str(exp))
            return jsonify({"status": 404}), 404

# GET/PUT/DELETE methods for Job object.
@api.route('/api/job/<int:jobid>', methods=['GET'])
@api.route('/api/job/<int:jobid>/<string:param>', methods=['GET'])
@api.route('/api/job/<int:jobid>', methods=['PUT'])
@api.route('/api/job/<int:jobid>', methods=['DELETE'])
def jobget(jobid, param="all"):
    if request.method == 'GET': # Checks current requested method.
        try:
            if param == "all":  # Check if specific paramater asked in GET endpoint
                return jsonify(crud.get_job(jobid)), 200
            else:
                return jsonify(crud.get_job(jobid)[param]), 200
        except Exception as exp:
            logging.exception("Exception:" + str(exp))
            return jsonify()

    if request.method == 'PUT': # Checks current requested method.
        try:
            receivedjson = request.get_json()   # Parse body sent as JSON
            return jsonify(crud.put_job(jobid, receivedjson)), 200
        except Exception as exp:
            logging.exception("Exception:" + str(exp))
            return jsonify({"status": 404}), 404

    if request.method == 'DELETE':  # Checks current requested method.
        try:
            return jsonify(crud.delete_job(jobid)), 200
        except Exception as exp:
            logging.exception("Exception:" + str(exp))
            return jsonify({"status": 404}), 404

