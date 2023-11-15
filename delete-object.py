import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Call S3 to delete an object from the bucket
def delete_object():
    try:
        bucket_name = input("Enter a bucket name: ")
        file_name = input("Enter a file name: ")
        s3.delete_object(Bucket=bucket_name, Key=file_name)
        print("File deleted successfully")

    except Exception as e:
        print(f"File deletion failed: {str(e)}")


delete_object()