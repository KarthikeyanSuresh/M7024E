import boto3

class InstanceStatus:
    """fill in the docstring"""

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



instance_status = InstanceStatus("eu-north-1")
print(instance_status.get_instance_status())