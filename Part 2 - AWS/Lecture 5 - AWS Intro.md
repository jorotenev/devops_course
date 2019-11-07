# Amazon Web Services - Intro & Core Services 
* AWS is currently holding the market cap in the cloud sector. It’s the de facto cloud provider with a market share of nearly 48% [[reference](https://www.businesswire.com/news/home/20190729005169/en/Gartner-Worldwide-IaaS-Public-Cloud-Services-Market) [reference](https://www.ciodive.com/news/iaas-Azure-AWS-Google-Cloud-Alibaba/559716/)]
* It was founded in 2006. It had a limited number of services in the beginning that had since grown significantly (165 services, as of 2019 [[reference](https://en.wikipedia.org/wiki/Amazon_Web_Services)])
* It provides a pay-as-you-go cloud infrastructure. It’s an IaaS (infrastructure as a service).
* IaaS means that the provider gives you the fundamental building blocks, rather than a full-fledged solution. You use the building blocks to compose your solution, rather being given the whole solution. For reference, there are companies which are Platform-as-a-Service - they enable you to just ship your code (e.g. via git) and just run it - PaaS is more focused on the application and the developer, rather than the underlying infrastructure. An example PaaS is Heroku. In Heroku you only need to provide a git repository with application code. Heroku will then deploy it for you on “dynos” and you have your app running. You don’t need to think about firewalls, networking, provisioning servers, patching, etc., etc.
* IaaS on the other hand gives you more flexibility for the price of added complexity.
* In recent years AWS has added services that resemble PaaS - e.g. BeanStalk where you can  provide a .zip with your code and BeanStalk will set up the servers, load balancers, networking for you.
* AWS is organized around services. Each service provides a given functionality - e.g. EC2 (elastic cloud computing) lets you run virtual machines on AWSs infrastructure, S3 lets you store files, etc. Services are integrated between each other so that building your own infrastructure is easier.
* Please be aware! AWS is a huge ecosystem. There’s a whole certification programme to prepare professionals to work with it. The certifications can be compared to a degree in terms of span and difficulty (e.g. the AWS Solutions Architect - Professional exam is considered as one of the toughest in the industry). There are hundreds of concepts in AWS. There’s an initial steep learning curve. However, when you grasp the most fundamental concepts, it gets easier - it’s easier to connect the dots when you know the basics and learning new services gets easier.
## AWS Fundamental Services and Concepts - High level overview
We will discuss the building blocks of AWS in brief. Those are the core services that you need to understand. Historically, they are also the first services to be added to AWS, signalling their importance.  
Having at least a basic understanding for all of the following services is vital if you want to work as a DevOps :)
### Elastic Cloud Computing (EC2)
EC2 is one of the core AWS services. It enables you to launch an instance in the cloud (the AWS term for a virtual machine). AWS has a huge bare metal capacity - actual, physical servers. You can launch your own instance on an actual server and use it as any other virtual computer - you can connect to it, install software on it - have full control over the OS. You can attach drives to the machine and access other instances within your network and connect to the internet. EC2 gives you full control over the configuration of your instance.  You can have instances with Windows and Linux (different distributions - e.g. Ubuntu, CentOS, etc.)

There are different types of instances in terms of their performance - cpu, ram, hdd & networking. You pay for what you use with high granularity (e.g. if you use the instance for 5 minutes, you pay only for those 5 minutes). The benefit of using EC2 is that you can scale up and down the number of instances that you run - e.g. if you know that you will receive huge traffic because of a marketing campaign - you can scale up your environment to handle the traffic.
### S3
Simple Storage Service or S3 is the file storage service of amazon. You can think of it as a super durable (i.e. your files are safe there) and theoretically unlimited FTP storage. It’s relatively cheap too - 1TB of storage can cost you as much as 22$ per month.
You can copy objects to and from S3 - e.g. from your PC to S3 and vice versa. You can copy objects within S3 too.
### VPC
Virtual Private Cloud. This is the service of AWS that enables you to create your network within the cloud. You can create subnets within your network, you can then launch instances within subnets. You can create rules that control the access to and from your network and subnets. E.g. you can make it so that a given instance can be accessed only from instances in the same subnet and disable access to the internet.  
You can have multiple networks within your account.  
When you say “VPC” you often mean the network created by the VPC service. 
### IAM
Identity and Access Management. This is another core service. Since you have many different services within AWS which are all doing various things, and you have users within your account (e.g. your developers, the DevOps team, etc.) you want to be able to control which user and service are allowed to perform what action. For example you might want to allow your DevOps team to start and terminate instances, but you want to forbid your QAs to do that.
All such permissions are handled within the IAM service. You can use the UI or write JSON to specify who can do what.

IAM is used everywhere in AWS so it’s vital to have working knowledge of it. 
AWS Regions & Availability Zones

AWS is huge. They have 22 regions. A region is some geographical area - e.g. Northern Virginia, Ireland, London, Frankfurt, etc. Each region has a name - us-east-1, eu-west-1, etc.
WIthin a region you have Availability Zones (AZ) - think of an AZ as a location within the region with a data center. There are typically 3 AZs within a region and are ~100km apart from each other. [[reference](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)]

The AZs in a region are interconnected via a high-bandwidth connection. This way you can run your production application across multiple AZs within a region - even if one of the AZs goes down - flood, earthquake, fire, etc., the app will continue running. You can do this by launching EC2 instances in multiple AZs within a region and distribute the application traffic across all instances. This way your application is said to be highly available - even in extreme circumstances (e.g. AZ down) it will continue working.

Regions are designed to be completely isolated from other regions. This has implications if you want to access a resource from one region to another. 

When you use AWS (from the UI, from the CLI or from programming languages) you need to specify which region you want to use. The regions are isolated in a way that you can think of them as separate “clouds”. In each region you have AWS services (EC2, etc.), each has its own physical infrastructure.
### ARN
Every resource in AWS has an identifier - be it a user, instance, bucket, subnet - virtually everything. It’s used to uniquely identify every possible resource in a given AWS account.
The format of an ARN is as follows [[reference](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html)]

`arn:<partition>:<service>:<region>:<account-id>:<resource-id>`

* partition is normally just “aws”
* service - s3, vpc, ec2, etc.
* region - e.g. eu-west-1, us-east-1, etc.
* account-id - the account in which the resource is
* resource-id - or the name of the resource. E,g, for an s3 bucket called “qa-bucket-progress” the * resource-id will just be that name. So for this bucket, given it’s in eu-west-1 and our account id is 123456 the arn of the bucket will be 
* arn:aws:s3:eu-west-1:123456:qa-bucket-progress
