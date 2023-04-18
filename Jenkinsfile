#!/usr/bin/env groovy

pipeline {
    agent any
    environment {
        ECR_REPO_NAME='node-app'
        EC2_SERVER ='52.63.4.66'
        EC2_USER='ec2-user'
        ECR_REGISTRY='044530424430.dkr.ecr.ap-southeast-2.amazonaws.com'
        DOCKER_USER='AWS'
        CONTAINER_PORT='8080'
        HOST_PORT='8080'
        AWS_DEFAULT_REGION = 'ap-southeast-2' 

        SSH_KEY_FILE=credentials('ec2-private-key')
        DOCKER_PWD=credentials('aws_ecr_repo_pwd')
        AWS_ACCESS_KEY_ID = credentials('aws_access_key_id')
        AWS_SECRET_ACCESS_KEY = credentials('aws_secret_access_key')

    }

    stages {
        stage('select the image version') {
            steps{
                script{
                    echo "fetching available images version from ecr repo"
                    def image_versions= sh(script:'python3 fetch-images.py', returnStdout:true).trim()
                    def tags_list=image_versions.split('\n') as List
                    version_to_deploy = input message:"Select version to deploy", ok:"Deploy", parameters:[choice(name:'Select version', choices: tags_list)]
                    echo "something"
                    echo version_to_deploy
                    env.DOCKER_IMAGE="${ECR_REGISTRY}/${ECR_REPO_NAME}:${version_to_deploy}"
                    echo env.DOCKER_IMAGE
                }
            }
        }

        stage('deploying image'){
            steps{
                script{
                    echo"deploying docker image to ec2 instance server"
                    def result = sh(script:"python3 deploy.py", returnStdout:true).trim()
                    echo result
                }
            }
        }
        stage('validate deployment'){
            steps{
                script{
                    echo "validating that the application was successfully deployed!"
                    def result=sh(script:"python3 validation-application.py", returnStdout:true).trim()
                    echo result
                }
            }
        }
    }
}