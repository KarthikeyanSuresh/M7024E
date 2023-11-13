import boto3

# Create an S3 client
s3 = boto3.client('s3')



def create_multiple_buckets():
    num_buckets = input("How many buckets do you want to create? ")
    for i in range(int(num_buckets)):
        bucket_name = input("Enter a bucket name: ")
        bucket_region = input("Enter a region: ")

        s3.create_bucket(Bucket=bucket_name, bucket_region=bucket_region)
        print("Bucket created successfully")
