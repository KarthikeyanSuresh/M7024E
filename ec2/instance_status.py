import boto3

class InstanceStatus:
    """
    This class is responsible for retrieving and printing the status of EC2 instances in a specified region using the AWS SDK boto3.
    
    Attributes:
        - ec2: A boto3 client representing Amazon EC2.
        - region: The AWS region in which to check the instance status.

    Methods:
        - get_instance_status(): Retrieves and prints the status of all EC2 instances in the specified region.
    """

    def __init__(self, region):
        self.ec2 = boto3.client('ec2', region_name=region) 
        self.region = region

    def get_instance_status(self):
        try:
            response = self.ec2.describe_instances()
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    instance_id = instance['InstanceId']
                    instance_state = instance['State']['Name']
                    print(f"Instance ID: {instance_id}, Status: {instance_state}")
        except Exception as e:
            print(f"Error getting instance status: {str(e)}") 

if __name__ == "__main__":
    region = str(input("Enter a region: "))
    instance_status = InstanceStatus(region)
    print(instance_status.get_instance_status())