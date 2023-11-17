import boto3

class ListBuckets:
    """
    A class to list S3 buckets in a specific region.

    Attributes:
        - region (str): The AWS region in which the S3 operations are performed.
        - s3 (boto3.client): The Boto3 S3 client for the specified region.

    Methods:
        - get_location(bucket_name): Returns the location of a given S3 bucket.
        - get_buckets_in_region(): Retrieves a list of S3 buckets in the specified region.
    
    """
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
