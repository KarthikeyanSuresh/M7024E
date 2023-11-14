import os
from s3.operations import S3Operations

filePath = '/Users/monicavasquez/Documents/LTU/Cloud Services/Lab2/Test'
files = ['seal.jpg']
buckets_regions = {'monvas-lab-1': 'eu-west-2'}

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