import boto3
import boto3


class CreateEC2Instance:
    def __init__(self, ami_id, instance_type, storage_size, region, instance_name, security_group, keypair):
        self.ami_id = ami_id
        self.instance_type = instance_type
        self.storage_size = storage_size
        self.region = region
        self.instance_name = instance_name
        self.security_group = security_group
        self.keypair = keypair
        self.ec2 = boto3.resource('ec2', region_name=region)
    
    def create_ec2_instance(self):
        # Create EC2 instance
        instance = self.ec2.create_instances(
            ImageId=self.ami_id,
            InstanceType=self.instance_type,
            KeyName=self.keypair,
            SecurityGroupIds=[self.security_group],
            
            MinCount=1,
            MaxCount=1,
            BlockDeviceMappings=[
                {
                    'DeviceName': '/dev/sda1',
                    'Ebs': {
                        'VolumeSize': self.storage_size
                    }
                }
            ], 
            TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': self.instance_name
                },
            ]
        },
    ],
        )
        
        return instance[0].id


if __name__ == "__main__":

    region = str(input("Enter a region: "))
    ami_id = str(input("Enter an AMI ID: "))
    instance_type = str(input("Enter an instance type: "))
    storage_size = int(input("Enter a storage size: "))
    instance_name = str(input("Enter an instance name: "))
    security_group = str(input("Enter a security group: "))
    keypair = str(input("Enter a keypair: "))
    instance = CreateEC2Instance(ami_id=ami_id, instance_type=instance_type, storage_size=storage_size, region=region, instance_name=instance_name, security_group=security_group, keypair=keypair)
    try:
        instance_id = instance.create_ec2_instance()
        print(f"Creating EC2 instance with ID: {instance_id}")
    except Exception as e:
        print(f"Error creating EC2 instance: {str(e)}")