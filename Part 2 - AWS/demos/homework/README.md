[![homework pipeline](https://i.ibb.co/7NVDCx5/homework-aws.png)](https://i.ibb.co/7NVDCx5/homework-aws.png)
# Homework
Всички инструкции за домашното са тук. Няма да ви се наложи да пишете никакъв код - всичко е написано вече. Ще ви отнеме около 10-15мин да навържете всички компоненти. Прегледайте целия flow и какво се случва, кой код какво прави - това е важното в домашното.  
Навсякъде по-долу заменете userX с вашия потребител.  
Най-долу има секция с обяснения кой файл/папка в това репо за какво е.

## Aim
Implement a Continues Deployment Pipeline using AWS Services.  The pipeline will deploy to Lambda our `userX-devops-lambda` application which consists of a Python file with the same content as the previous homework lambda (printing contents of a file). Each time we make a change to our project and push it, a CD pipeline will trigger which will deploy our changes.
## End result
1. The pipeline is triggered by pushing a commit to a CodeCommit repository (`userX-devops-lambda`)
1. The commit triggers an event to a worker lambda (whose code is in `trigger_codebuild.py`). The worker lambda will extract the branch to which we have pushed and the commit id. It will start a CodeBuild build and it will pass the branch and commit as environmental variables to the build
1. CodeBuild will simply [package](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/package.html) the contents of the repository. The `package` command will add the `CodeURI` property of the Lambda within the CloudFormation template (i.e. a new version of the template will be generated where CodeURI of the lambda resource will point to a S3 object. The CodeUri property points to the location of the zipped code of the lambda). 
1. (done for you :) ) From CodeBuild we will create/update a CloudFormation stack with the updated version of the yaml template from our repo
1. (done for you :) ) CloudFormation will deploy the `userX-devops-lambda` Lambda code for us


# Steps
* go to IAM -> find your user. Go to Security Credentials and generate HTTPS CodeCommit Credentials - save them to your computer
* create a CodeCommit repo called `userX-devops-lambda` where userX is your username
* Prepare the repo
    * on your computer `git clone` the repo. The command will be  
    `git clone https://git-codecommit.eu-west-1.amazonaws.com/v1/repos/userX-devops-lambda # REPLACE userX` 
        * use the credentials that you downloaded from the IAM credentials step above when asked
    * add the buildspec.yml + template.yml files in the root directory of your repo (e.g. C:/..../userX-devops-lambda) (copy them from this repos' repo_content/)
        * don't add the lambda file for now.
    * `git add .` # stage the new files
    * `git commit -m "Initial Commit"` # commit the staged files
    * `git push origin master` # this will push the commit to CodeCommit 
    * if you open your CodeCommit repo from AWS UI, you should see the two files
* Create your CodeBuild project
    * go to CodeBuild -> Build Projects -> Create
    * Project name: `userX-devops-lambda` # !! Change userX
    * Source: CodeCommit -> your repo 
    * "Branch: (Choose a branch that contains the code to build)": master
    * Environment: 
        * Managed image
        * Operating system: Ubuntu
        * Runtime: Standard
        * Image: 4.0
        * Service role: Existing role -> arn:aws:iam::750385577863:role/codebuild-role-homework
        * !!! Remove the tick from "Allow AWS CodeBuild to modify this service role..."
    * Buildspec -> Use a buildspec file
        * by default it will use the `buildspec.yml` from your repository. Note: you can insert commands from this screen too, if you don't have control over the contents of the repo. In this case the repo is yours so we'll read the buildspec from the buildspec.yml in the repo
    * leave the other options
    * Click `Create`
* Create the trigger-codebuild worker lambda.:
    * add a lambda called `userX-worker-trigger-codebuild`
    * use Python 3.7
    * Select the "Choose or create an execution role" and use the arn:aws:iam::750385577863:role/progressbg-lambda-role 
    * Paste the code from `trigger_codebuild.py` in this repo in the lambda_function file
    * Add trigger
        * Type: CodeCommit
        * Repository Name -> choose your repo
        * triggername - write some trigger name
        * Events -> Push to existing branch
        * leave the default "all existing branches"
* add the `repo_content/lambda_function.py` file to your repo as just lambda_function.py, commit it and push it
* then open the CodeBuild project's dashboard - a build should be happening - open it to see the logs
* then open CloudFormation - if the build succeeded, a stack called `userX-devops-lambda` was created
* from the stack's Resources, open the Lambda - ensure it has the code you expect :)
* add an extra print statement or a comment or whatever to your code (in the `userX-devops-lambda` repo), then push it. After the build succeeds, you will see the new changed applied in your Lambda.
* that's it :)



# Repo contents
In the current folder is the code for all resources needed to complete successfuly the homework:
- under `repo_content/`
    - this is sample of a "software project" repo - i.e. a project/product for which you want to have CI/CD
    - the code of our `userx-devops-lambda` (under `repo_content/lambda_handler.py`)
    - the yaml of our CloudFormation template (under `repo_content/template.yml`)
    - a `buildspec.yml` - defines what to do during a build. the buildspec actually is just getting
    bash scripts from s3 and executing them
- under `codebuild/` - the files are just for your reference - you don't need to use them anywhere
    - bash files which are already uploaded to S3 and are executed during each CodeBuild build process. in the buildspec.yml, the files from this folder are downloaded and executed
- `trigger_codebuild.py` the code of the worker Lambda which will receive the push event from CodeCommit and trigger CodeBuild
    - this lambda will intercept commit to your git repo and trigger a CodeBuild build

# EXTRA POINTS
Make a commit to your repo's template.yml that will subscribe it for Upload/Modify events from a given S3 bucket
