import boto3
import json

client = boto3.client("ecs", region_name="us-east-1")

clusters = client.list_clusters()

cluster_name = clusters['clusterArns'][0]

response = client.create_service(cluster=cluster_name,
                                 serviceName="SimpleWebServer",
                                 taskDefinition='console-sample-app',
                                 desiredCount=1,
                                 networkConfiguration={
                                     'awsvpcConfiguration': {
                                         'subnets': [
                                             'subnet-9e7c0fc1',
                                         ],
                                         'assignPublicIp': 'ENABLED',
                                         'securityGroups': ["sg-0bfa5becbde957cd3"]
                                     }
                                 },
                                 launchType='FARGATE',
                                 )

print(json.dumps(response, indent=4, default=str))