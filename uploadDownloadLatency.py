import os
from s3.operations import S3Operations

filePath = os.getcwd() + '/Test'
files = ['1','10','100','500']
buckets_regions = {'monvas-lab-1': 'eu-west-2','mssm3': 'ap-south-1', "bri-l2-bucket-eu-north-1":'eu-north-1'}

def latencyTest():
    # Upload objects to S3 bucket
    for file in files:
        local_file_path = os.path.join(filePath, file)
        objectKey = file
        uploadTest(local_file_path,objectKey)

    # Download objects to S3 bucket
        object_name = file
        downloadTest(objectKey, object_name)


def uploadTest(local_file_path,objectKey):
    for bucket,region in buckets_regions.items():
        s3_ops_region = S3Operations(region)
        s3_ops_region.upload_s3_object(local_file_path, bucket, objectKey)

def downloadTest(objectKey, objectName):
    for bucket,region in buckets_regions.items():
        s3_ops_region = S3Operations(region)
        s3_ops_region.download_s3_object(bucket, objectKey, objectName)

if __name__ == '__main__':
    latencyTest()