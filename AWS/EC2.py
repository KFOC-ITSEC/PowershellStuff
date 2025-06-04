import boto3
from botocore.exceptions import ClientError

aws_access_key_id = "AKIAUM4G6O6NIMEU2T25"
aws_secret_access_key = "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"
region_name = "us-east-2"

def list_ec2_instances():
    try:
        ec2 = boto3.client(
            'ec2',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )

        response = ec2.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
    except ClientError as e:
        print("Failed to connect to AWS EC2:", e)

if __name__ == "__main__":
    list_ec2_instances()
