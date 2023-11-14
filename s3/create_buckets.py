import boto3

class CreateBuckets:
    def __init__(self, bucketName, region):
        self.region = region
        self.bucketName = bucketName
        self.s3 = boto3.client('s3', region_name=self.region)

    def create_bucket(self):
        try:
            # Check if bucket with name exists already
            buckets = self.s3.list_buckets()['Buckets']
            for bucket in buckets:
                if self.bucketName == bucket['Name']:
                    print(f"Bucket '{self.bucketName}' already exists. Choose a different name.")
                    return
            
                # Create the bucket with the specified region
                else:
                    self.s3.create_bucket(Bucket=self.bucketName, CreateBucketConfiguration={'LocationConstraint': self.region})
            print("Bucket created successfully")

        except Exception as e:
            print(f"Bucket creation failed: {str(e)}") 

