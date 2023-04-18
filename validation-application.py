import requests
import time
import os

ssh_host=os.environ['EC2_SERVER']
host_port=os.environ['HOST_PORT']

#validate the application started successfully

try:
    time.sleep(20)
    response = requests.get(f"http://{ssh_host}:{host_port}")
    if response.status_code == 200:
        print("The node application is running successfully!")
    else:
        print("The node application deployment was not successful!")


except Exception as ex:
    print(f"Connection error happened:{ex}")
    print("Application not accessible at all!")