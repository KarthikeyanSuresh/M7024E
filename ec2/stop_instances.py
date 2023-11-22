import boto3
from instance_status import InstanceStatus

class StopInstances:
    """
    This class is responsible for stopping EC2 instances using the AWS SDK boto3.
    
    Attributes:
        - ec2: A boto3 client representing Amazon EC2.
        - instance_id (str): The ID of the EC2 instance to be stopped.

    Methods:
        - stop_instance(instance_id): Stops the specified EC2 instance.
    """

    def __init__(self):
        self.ec2 = boto3.client('ec2') 

    def stop_instance(self, instance_id):    
        try:
            response = self.ec2.stop_instances(InstanceIds=[instance_id])
            print(f"Instance {instance_id} is stopping now.")
            # print("Response:", response)
        except Exception as e:
            print(f"Error stopping instance {instance_id}: {str(e)}") 


if __name__ == "__main__":
    region = str(input("Enter a region: "))
    instance_status = InstanceStatus(region)
    print(instance_status.get_instance_status())

    num_instances = int(input("Enter the number of instances to stop: "))
    for i in range(num_instances):
        inst = StopInstances()
        instance_id = str(input("Enter an Instance ID: "))
        try:
            inst.stop_instance(instance_id)
        except Exception as e:
            print(f"Error stopping instance: {str(e)}")
