import os
from s3.operations import S3Operations
from s3.list_buckets import ListBuckets
from s3.create_buckets import CreateBuckets

def run():
    print("The following actions are available: 1. Create S3 buckets, 2. List S3 buckets, 3. Operations in S3")
    action = input("Enter the number of the action you want to perform: ")

    # Create S3 buckets
    if action == "1":
        create_bucket()

    # List S3 buckets
    if action == "2":
        list_buckets()

    # Operations in S3
    if action == "3":
        operations_in_s3()
     

def create_bucket():
    num_buckets = input("How many buckets do you want to create?: ")
    for num in num_buckets:
        bucket_name = input("Enter a bucket name: ")
        bucket_region = input("Enter a region: ")
        # Instantiate CreateBuckets class
        s3_bucket_creation = CreateBuckets(bucket_name,bucket_region)
        s3_bucket_creation.create_bucket()  

def list_buckets():
    # Get the region from the user 
    region = input("Enter region to list the existing buckets in that region: ")
    # Instantiate ListBuckets class
    s3_bucket_list = ListBuckets(region)
    # Output the bucket names in the specified region
    print("The list of existing buckets in the " + region + " are:")
    for bucket in s3_bucket_list.get_buckets_in_region():
        print(bucket)

def operations_in_s3():
   # Operations in S3
    print("Operations Available: 1. Upload, 2. Download and 3. Delete objects in S3")
    operation = input("Enter the number of the operation you want to perform: ")
    bucket_name = input("Enter the bucket name: ")
    region_operation = input("Enter the region: ")

    # Instance of S3Operations class
    s3_operations = S3Operations(region_operation)

    # Upload objects to S3 bucket
    if operation == "1":
        file_path = input("Enter the file path: ")
        object_key = input("Enter the object key: ")
        s3_operations.upload_s3_object(file_path, bucket_name, object_key)

    # Download objects from S3 bucket
    if operation == "2":
        object_name = input("Enter the name of the file to be downloaded: ")
        object_key = input("Enter the object key: ")
        s3_operations.download_s3_object(bucket_name, object_key, object_name) 

    # Delete objects from S3 bucket

if __name__ == '__main__':
    run()



