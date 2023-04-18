import os
import boto3
aws_ecr_repo_name = os.environ['ECR_REPO_NAME']


#get all ecr in sydney region, is default
ecr_client=boto3.client('ecr')

images=ecr_client.describe_images(repositoryName=aws_ecr_repo_name)

image_tags=[]
for image in images['imageDetails']:
    image_tags.append(image['imageTags'][0])

#send the output into console
for tag in image_tags:
    print(tag)