# progressbg.net Final Assignment
Assignment for the Progress DevOps

# Task
Build and deploy a web application which exposes an API. The API will send a text message (SMS) to a given phone number with provided content. The sms is sent via the AWS SNS service.

To achieve this, you will create the following stack:
![Visual](.github/progress-final.png?raw=True "Assignment")


All the neccessary steps will be described below + most of the code that you will need.  
This repository contains the code snippets that you will need. 
# Prerequisites
* please ensure you have boto3 and docker installed on your system

# Steps
## High-level overview
* Build Docker image from a Dockerfile which contains our python web app that will serve the API requests
* Create an ECR (Elastic Container Registry) repository where you will upload you docker image (name it `userX-sms-app`)
* Push the image you'll build to your ECR repository
* Create an IAM instance role which will give access to SNS and ECR (name the role `userX-sms-app`)
* Create an **Ubuntu 16.04** EC2 instance and give it the above IAM role so that the instance can use SNS
* On the instance, install docker. then start a container by using the image you've pushed to your ECR repository
* Get your sever's IP and access it via a browser :)
* Voilà

## Detailed steps
## Initial setup
To begin with the assignment you need to clone this repository to your computer.

```
git clone https://github.com/jorotenev/progress_final_assignment.git 
```
The above command will clone this repo to your computer in the `progress_final_assignment` folder.
## To create an ECR docker image repository
Go to the AWS UI, go to ECR and create a repository with the name as follows `userX-sms-app`

## Build docker image
* via your shell go to the `python-application` folder
* go to your ECR repo and click the View push commands button on the right
* follow the steps to build, tag & push your image. 
    * NOTE!! if you can't login just execute `aws ecr get-login --no-include-email --region eu-west-1`, copy the output and execute it 
## To create an IAM instance role
When creating the role, for "Choose the service that will use this role" select EC2.
Then attach the following Policies to the role to allow access to SNS and ECR:
* `AmazonSNSFullAccess`
* `AmazonEC2ContainerRegistryReadOnly`
## Install pip & aws-cli on Ubuntu
pip is the python package manager - it lets us use python packages
```
sudo apt-get update
sudo apt-get install python3-pip -y
```

The AWS CLI is actually a python package with a CLI interface. We will install it with pip
```
pip3 install awscli --upgrade --user
```

## Run the docker container
### Install docker
* go to the official docs and follow the [instructions](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* don't forget to add your ubuntu user to the docker group. This way you don't need to prefix all docker commands with sudo :)
`sudo usermod -aG docker ubuntu`
* check your installatio via 
`docker -v # you should see the installed version`
    * if it fails, from mremoteng, try to reconnect to the instal (on the tab -> Reconnect)

### Run instructions
We need to run the docker image with the following requirements: 
- map the host port 80 to the container port 5000
- pass the AWS_DEFAULT_REGION=eu-west-1 environmental variable
see the `docker run` documentation on how to do this

Don't forget to login to ECR from your instance too.
`$(aws ecr get-login --no-include-email --region eu-west-1)`