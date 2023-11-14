import boto3
import os
import time

class S3Operations:
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

# download_s3_object('monvas-lab-1', 'seal.jpg', 'seal.jpg')

# filePath = '/Users/monicavasquez/Documents/LTU/Cloud Services/Lab2/Test'
# files = ['seal.jpg']

# for file in files:
#     local_file_path = os.path.join(filePath, file)
#     upload_s3_object(local_file_path, 'monvas-lab-1', file)

