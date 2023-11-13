import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Call S3 to create the buckets
def create_multiple_buckets():
    num_buckets = input("How many buckets do you want to create? :")
    for i in range(int(num_buckets)):
        try:
            bucket_name = input("Enter a bucket name: ")
            bucket_region = input("Enter a region: ")
            # Check if bucket with name exists already
            buckets = s3.list_buckets()['Buckets']
            for bucket in buckets:
                if bucket_name == bucket['Name']:
                    print(f"Bucket '{bucket_name}' already exists. Choose a different name.")
                    return
            
                # Create the bucket with the specified region
                else:
                    
                    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': bucket_region})
            print("Bucket created successfully")

        except Exception as e:
            print(f"Bucket creation failed: {str(e)}") 


create_multiple_buckets()



