"""File Manager for S3 End-Point Namespace.

Provides the mount point for all of operation end-points.
"""
from flask_restplus import Namespace

api = Namespace('fileManager', description='API for Managing files in S3')