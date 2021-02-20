import boto3
from botocore.exceptions import ClientError
import logging
from api.services import BUCKET, DOWNLOAD_DIR, UPLOAD_DIR


class AccessBucket:
    def upload_file(self,file_name):
        """
        Function to upload a file to an S3 bucket
        """
        object_name = file_name
        s3_client = boto3.client('s3', use_ssl=False)
        filename_path = f"{UPLOAD_DIR}/{file_name}"
        try:
            response = s3_client.upload_file(filename_path, BUCKET, object_name)
        except ClientError as e:
            logging.error(e)
            return None
        return object_name

    def download_file(self, file_name):
        """
        Function to download a given file from an S3 bucket
        """
        s3 = boto3.resource('s3', use_ssl=False)
        output = f"{DOWNLOAD_DIR}/{file_name}"
        try:
            s3.Bucket(BUCKET).download_file(file_name, output)
        except ClientError as e:
            logging.error(e)
            return None

        return output


    def list_files(self, bucket):
        """
        Function to list files in a given S3 bucket
        """
        s3 = boto3.client('s3', use_ssl=False)
        contents = []
        for item in s3.list_objects(Bucket=bucket)['Contents']:
            contents.append(item)

        return contents
