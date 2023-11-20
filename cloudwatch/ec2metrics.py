import boto3
from datetime import date, timedelta, datetime
import random

class CloudwatchMetrics:
    def __init__(self,region):
        self.region = region
        self.cloudwatch = boto3.client('cloudwatch',region_name=self.region)

    def get_ec2_metrics(self, instance_id, metric_name, period = 300):
        try:
            random_numbers = random.sample(range(1, 9), 8)
            concatenated_string = ''.join(map(str, random_numbers))
            metric_id = 'm'+concatenated_string
            
            end_time=datetime.utcnow()
            start_time=end_time - timedelta(minutes=5)

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
    
