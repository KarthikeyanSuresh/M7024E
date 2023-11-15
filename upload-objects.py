import logging
import boto3
from botocore.exceptions import ClientError
import os



def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def upload_files():

    num_files = int(input("Enter the number of files to upload: "))
    for i in range(num_files):
        try:
            file_name = input("Enter the file name to upload: ")
            bucket_name = input("Enter the bucket name to upload the file to: ")
            upload_file(file_name, bucket_name)
            print("File uploaded successfully")
        except Exception as e:
            print(f"File upload failed: {str(e)}") 
   
upload_files()
