import boto3
from datetime import date, timedelta, datetime
import random

class CloudwatchMetrics:
    """
    The CloudwatchMetrics class provides methods to fetch EC2 metrics from AWS CloudWatch.

    This class uses the boto3 library to interact with the AWS CloudWatch service. It provides
    a method to get EC2 metrics for a specific instance.

    Attributes:
        region (str): The AWS region where the CloudWatch client will be created.
        cloudwatch (boto3.CloudWatch): The CloudWatch client.

    Methods:
        get_ec2_metrics(instance_id: str, metric_name: str, period: int) -> float:
            Fetches a specific metric for a specific EC2 instance.
    """
    def __init__(self,region):
        """
        Initializes a new instance of the CloudwatchMetrics class.

        Args:
            region (str): The AWS region where the CloudWatch client will be created.
        """
        self.region = region
        self.cloudwatch = boto3.client('cloudwatch',region_name=self.region)

    def get_ec2_metrics(self, instance_id, metric_name, period):
        """
        Fetches a specific metric for a specific EC2 instance.

        Args:
            instance_id (str): The ID of the EC2 instance.
            metric_name (str): The name of the metric to fetch.
            period (int): The period in seconds over which the metric is applied.

        Returns:
            float: The value of the metric, or None if the metric could not be fetched.
        """
        try:
            random_numbers = random.sample(range(1, 9), 8)
            concatenated_string = ''.join(map(str, random_numbers))
            metric_id = 'm'+concatenated_string
            
            end_time=datetime.utcnow()
            start_time=end_time - timedelta(minutes=period/60)

            response = self.cloudwatch.get_metric_data(
                MetricDataQueries=[
                    {
                        'Id': metric_id,
                        'MetricStat': {
                            'Metric': {
                                'Namespace': 'AWS/EC2',
                                'MetricName': metric_name,
                                'Dimensions': [
                                    {
                                        'Name': 'InstanceId',
                                        'Value': instance_id
                                    },
                                ]
                            },
                            'Period': period,
                            'Stat': 'Average'
                        },
                        'ReturnData': True,
                    },
                ],
                StartTime=start_time,
                EndTime=end_time,
            )

            if 'MetricDataResults' in response and response['MetricDataResults'][0]['Values']:
                return response['MetricDataResults'][0]['Values'][0]

            else:
                return None

        except Exception as e:
            print(e)
    
