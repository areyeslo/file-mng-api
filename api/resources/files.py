import os
from flask import request, redirect, send_file
from flask import make_response
from flask_restx import Namespace, Resource
import json

from ..services import UPLOAD_DIR
from ..services.access_files import AccessBucket
from ..utils.util import cors_preflight
from ..utils.api_resource import get_query_param_str

"""
File Manager for S3 End-Point Namespace.
Provides the mount point for all of operation end-points.
"""
api = Namespace('fileManager', description='API for Managing files in S3')

upload_directory = os.getenv('UPLOAD_DIRECTORY')
bucket = os.getenv('BUCKET')


@cors_preflight('GET')
@api.route('/buckets', strict_slashes=False, methods=['GET', 'OPTIONS'])
class Buckets(Resource):
    @staticmethod
    def get():
        service = AccessBucket()
        contents = service.list_files("{}".format(bucket))
        payload = json.dumps(contents, indent=4, sort_keys=True, default=str)
        response = make_response(payload, 200)

        return response


@cors_preflight('POST, GET')
@api.route('/file', methods=['POST', 'GET', 'OPTIONS'])
class File(Resource):
    @staticmethod
    @api.doc(params={
        'filename': 'Filename to upload to S3'
    })
    def post():
        service = AccessBucket()
        filename = get_query_param_str('filename')
        service.upload_file(filename)

        return None

    @staticmethod
    @api.doc(params={
        'filename': 'Filename to download to S3'
    })
    def get():
        filename = get_query_param_str('filename')
        service = AccessBucket()
        output = service.download_file(filename)

        return send_file(output, as_attachment=True)
