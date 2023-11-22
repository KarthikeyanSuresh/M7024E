import boto3
from instance_status import InstanceStatus

class StopInstances:
    """fill in the docstring"""

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
    region = str(input("Enter only a region: "))
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
