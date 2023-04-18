### Project Description

Create a Jenkins job that fetches all the available images from your application's ECR repository using Python. It allows the user to select the image from the list through user input and deploys the selected image to the EC2 server using Python.

### Technologies Used:
Python, boto3, paramiko, git

### Task:
1- Fetch all 3 images from the ECR repository (using Python)

2- Let the user select the image from the list (hint: https://www.jenkins.io/doc/pipeline/steps/pipeline-input-step/)

3- SSH into the EC2 server (using Python)

4- Run docker login to authenticate with ECR repository (using Python)

5- Start the container from the selected image from step 2 on EC2 instance (using Python)

6- Validate that the application was successfully started and is accessible by sending a request to the application (using Python)

### Usage Instruction:

###### Step 1: Preparation:

1- Deploy and configure a EC2 instance server with port 22 open for SSH in AWS.
![image](images/Screenshot%202023-04-18%20at%209.23.51%20am.png)

2- Install Docker on the Droplet server.
![iamge](images/Screenshot%202023-04-18%20at%209.26.04%20am.png)

3- Install Python, pip and related dependencies, such as boto3, requests, paramiko via root user
```
apt update
apt install python3
apt install pip
pip install boto3
pip install paramiko
pip install requests
```
![image](images/Screenshot%202023-04-18%20at%209.50.17%20am.png)
 ![image](images/Screenshot%202023-04-18%20at%209.52.09%20am.png)
 ![image](images/Screenshot%202023-04-18%20at%209.52.39%20am.png)
 ![image](images/Screenshot%202023-04-18%20at%209.53.07%20am.png)
4- Prepare 3 Docker images with tags 1.0, 2.0, 3.0 in AWS ECR
![image](images/Screenshot%202023-04-18%20at%209.20.44%20am.png)

###### Step 2: Deploy and configure Jenkins server

1- Create a jenkins server as a container in Droplet server and bind mount Docker with it.

2- Configure the credentials inside Jenkins UI

```
"jenkins_aws_access_key_id" - Secret Text
"jenkins_aws_secret_access_key" - Secret Text
"ssh-creds" - SSH Username with private key
"ecr-repo-pwd" - Secret Text
```
3-Install ssh agent plugin in Jenkins UI

###### Step3: 