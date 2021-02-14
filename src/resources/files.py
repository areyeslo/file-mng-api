import os
from flask import Flask, render_template, request, redirect, send_file
from flask import make_response, jsonify
from flask_restx import Namespace, Resource, cors
from src.services.access_files import AccessBucket
from src.utils.util import cors_preflight
from .api_namespace import api

upload_directory = os.getenv('UPLOAD_DIRECTORY')
bucket = os.getenv("BUCKET")


@cors_preflight("GET")
@api.route('/', strict_slashes=False, methods=['GET', 'OPTIONS'])
class FileManager(Resource):
    @staticmethod
    @cors.crossdomain(origin='*')
    def get_buckets():
        service = AccessBucket()
        contents = service.list_files("{}".format(bucket))
        payload = contents.to_json()
        response = make_response(payload, 200)

        return response


    # @cors_preflight('POST')
    # @cors.crossdomain(origin='*')
    # def upload():
    #     if request.method == "POST":
    #         service = AccessBucket()
    #         f = request.files['file']
    #         f.save(os.path.join(upload_directory, f.filename))
    #         service.upload_file(f"{0}{1}".format(upload_directory, f.filename), bucket)
    #
    #         return redirect("/storage")
    #
    # @cors_preflight('GET')
    # @cors.crossdomain(origin='*')
    # @api.doc(params={
    #     'name': 'A company / organization name string',
    #     'location': 'A location code [ BC (only)]',
    #     'entity_type_cd': 'An entity type code [ CR, UL, CC ]',
    #     'request_action_cd': 'A request action code [ NEW ]'
    # })
    # def download(filename):
    #     if request.method == 'GET':
    #         service = AccessBucket
    #         directory = os.getenv()
    #         output = service.download_file(directory, filename, bucket)
    #
    #         return send_file(output, as_attachment=True)

