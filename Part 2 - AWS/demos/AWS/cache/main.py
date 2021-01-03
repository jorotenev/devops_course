from flask import Flask
import redis
from boto3 import client
from os import environ

app = Flask(__name__)
redis_client = redis.Redis(
    host='redishost',
    port=6379,
)
@app.route('/<region>')
def hello_world(region):
    lambdas = get_from_cache(region)
    if not lambdas:
        lambdas = get_lambdas_from_aws(region)
        put_in_cache(region, lambdas)
    return lambdas


def get_from_cache(region):
    return redis_client.get(region)


def put_in_cache(region, content):
    redis_client.set(region, content)


def get_lambdas_from_aws(region):
    lambda_api = client('lambda', region_name=region, aws_access_key_id=environ['AWS_KEY'],
                        aws_secret_access_key=environ["AWS_SECRET"])
    response = lambda_api.list_functions()
    return str([func['FunctionName'] for func in response['Functions']])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True)