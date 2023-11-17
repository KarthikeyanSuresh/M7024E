import boto3

class DeleteS3Object:
    def __init__(self, bucket_name, file_name):
        self.s3 = boto3.client('s3')
        self.bucket_name = bucket_name
        self.file_name = file_name

    # Function to delete an object from the S3 bucket
    def delete_object(self, bucket_name, file_name):
        try:
            self.s3.delete_object(Bucket=bucket_name, Key=file_name)
            print("File deleted successfully")
        except Exception as e:
            print(f"File deletion failed: {str(e)}")
