from cloudwatch.ec2metrics import CloudwatchMetrics

class EC2Operations:
    def fetch_metrics(self, ec2_metrics, instance_id, metric_name):
        if instance_id and metric_name:
            data_points = ec2_metrics.get_ec2_metrics(instance_id, metric_name)
            return data_points
        else:
            return None