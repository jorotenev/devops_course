import json
import boto3


def lambda_handler(event, context):
    print(event)
    s3 = boto3.resource('s3')
    bucketname = event['Records'][0]['s3']['bucket']['name']
    filename = event['Records'][0]['s3']['object']['key']

    obj = s3.Object(
        bucketname,
        filename
    )
    print(obj.get()['Body'].read())
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
