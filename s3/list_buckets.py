import boto3

class ListBuckets:
    def __init__(self, region):
        self.region = region
        self.s3 = boto3.client('s3', region_name=self.region)
        
    # Function to get the location of an S3 bucket
    def get_location(self, bucket_name):
        response = self.s3.get_bucket_location(Bucket=bucket_name)
        return response['LocationConstraint']

    # Function to get the list of buckets in a region
    def get_buckets_in_region(self):
        buckets = []
        response = self.s3.list_buckets()
        for bucket in response['Buckets']:
            location = self.get_location(bucket['Name'])
            if location == self.region:
                buckets.append(bucket['Name'])
        return buckets

# # Get the region from user input
# print("Enter region to list the existing buckets in that region: ")
## region = input()

# # Output the bucket names in the specified region
# print("The list of existing buckets in the " + region + " are:")
# buckets = get_buckets_in_region(s3, region)
# for bucket in buckets:
#     print(bucket)
