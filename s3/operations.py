import boto3
import os
import time

class S3Operations:
    """
    This class handles operations related to AWS S3. It includes methods to upload, download, and delete objects in an S3 bucket.

    Attributes:
        region (str): The AWS region where the S3 bucket is located.
        s3 (boto3.client): The boto3 S3 client.

    Methods:
        upload_s3_object(filePath, bucketName, objectKey): Uploads a file to an S3 bucket.
        download_s3_object(bucketName, objectKey, objectName): Downloads a file from an S3 bucket.
        delete_s3_object(bucket_name, file_name): Deletes a file from an S3 bucket.
    """

    # Initialize the S3 client
    def __init__(self, region):
        self.region = region
        self.s3 = boto3.client('s3', region_name=self.region)

    # Upload objects to S3 bucket
    def upload_s3_object(self,filePath, bucketName, objectKey):
        try:
            start_time = time.time()
            self.s3.upload_file(filePath, bucketName, objectKey)
            end_time = time.time()
            upload_latency_sec = (end_time - start_time)
            print("%s File Upload Successful to Bucket %s. Upload time: %s seconds" %(objectKey, bucketName, upload_latency_sec))
        except Exception as e:
            print(e)

    # Download objects from S3 bucket
    def download_s3_object(self,bucketName, objectKey, objectName):
        try:
            start_time = time.time()
            self.s3.download_file(bucketName, objectKey, objectName)
            end_time = time.time()
            download_latency_sec = (end_time - start_time)
            print("%s File Download Successful from Bucket %s. Download time: %s seconds" %(objectKey,bucketName,download_latency_sec))
        except Exception as e:
            print(e)

    # Delete objects from S3 bucket
    def delete_s3_object(self, bucket_name, file_name):
        try:
            self.s3.delete_object(Bucket=bucket_name, Key=file_name)
            print("File deleted successfully")
        except Exception as e:
            print(f"File deletion failed: {str(e)}")


