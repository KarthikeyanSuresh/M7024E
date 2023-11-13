import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Function to get the location of an S3 bucket
def get_location(client, bucket_name):
    response = client.get_bucket_location(Bucket=bucket_name)
    return response['LocationConstraint']

# Function to get the list of buckets in a region
def get_buckets_in_region(client, region):
    buckets = []
    response = client.list_buckets()
    for bucket in response['Buckets']:
        location = get_location(client, bucket['Name'])
        if location == region:
            buckets.append(bucket['Name'])
    return buckets

# Get the region from the user 
print("Enter region to list the existing buckets in that region: ")
region = input()

# Output the bucket names in the specified region
print("The list of existing buckets in the " + region + " are:")
buckets = get_buckets_in_region(s3, region)
for bucket in buckets:
    print(bucket)
