import boto3

def client_init():
    client = boto3.client('ec2', region_name='eu-central-1')
    return client

def vpc_creation(client):
    client.create_vpc(idrBlock='10.0.0.0/16')

if __name__=="__name__":
    client = client_init()
    vpc_creation(client)