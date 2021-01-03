from boto3 import client
def lambda_handler(event, context):
    codebuild = client('codebuild')
    # index -1 takes the last element of a list
    # split() splits a string into a list based on a delimiter
    repo = event['Records'][0]['eventSourceARN'].split(':')[-1]
    commit_info = event['Records'][0]['codecommit']['references'][0]
    branch_raw = commit_info['ref']
    commit = commit_info['commit']
    branch = branch_raw.split('/')[-1]

    response = codebuild.start_build(
        projectName=repo,
        sourceVersion= commit,
        environmentVariablesOverride=[
            {
                'name': 'COMMIT',
                'type': 'PLAINTEXT',
                'value': commit
            },
            {
                'name': 'BRANCH',
                'type': 'PLAINTEXT',
                'value': branch
            },
            {
                'name': 'APP',
                'type': 'PLAINTEXT',
                'value': repo
            },
        ]
    )
    print(response)
    return response['build']['buildStatus']



if __name__ == '__main__':
    sample_event = {
  "Records": [
    {
      "awsRegion": "eu-west-1",
      "codecommit": {
        "references": [
          {
            "commit": "ad4334c0",
            "ref": "refs/heads/master"
          }
        ]
      },
      "eventId": "38e06347-cd68-4141-b601-f814a6b06318",
      "eventName": "TriggerEventTest",
      "eventPartNumber": 1,
      "eventSource": "aws:codecommit",
      "eventSourceARN": "arn:aws:codecommit:eu-central-1:740650266824:user8-devops-lambda",
      "eventTime": "2019-10-01T11:06:05.409+0000",
      "eventTotalParts": 1,
      "eventTriggerConfigId": "..",
      "eventTriggerName": "trigger-codebuild",
      "eventVersion": "1.0",
      "userIdentityARN": "arn:..."
    }
  ]
}