
# Lecture 1 & 2 - Bash & Python
## ​1.1​ Intro

Why are we here
---
To get productive. To be able to automate mission critical parts of the IT infrastructure at our day jobs (or future jobs)  
Learn how to build cloud infrastructure and automate this process via infrastructure-as-a-code.  
Focus is on being productive and establish a mental model of what’s happening and why.  
We won’t cover everything. 
* time-limit
* I don’t know everything :)  

Interactive format of the sessions. All of the content - I have written it down so you don’t have to. Focus is on active listening and engaging.
If you don’t ask questions - I’m doing something wrong. :)

## ​1.2​ Lecture 1

### 1.2.1​ Why DevOps?
What is the problem that we are trying to solve? What’s the end state that we are aiming to? 
We want to manage complexity, reduce errors and increase developer productivity. 
We want to have an infrastructure that we can easily recreate if needed, be able to monitor it so we know its state. 
We want to make deployments easy & repeatable. We want to reduce the human-error factor. Deploying should be as easy as pressing a button. Rollback should be just as easy.  
We want to have an infrastructure that is as cost-efficient as possible and easy to adapt to the ever changing business requirements.  
#### How was it done before, what’s the state now?
* Before - the developer gives the operations team the code and then ops need to figure out how to make this thing run in prod without getting phone calls during the night. Hard - the dev has a different environment (e.g. OS, installed packages, etc). This leads to dev-vs-ops pressure and lack of shared responsibility. Risky, manual deployments of large changesets - e.g. deployment cycle every month.
* Now - we aim to automate the release process. Aim is to have as much as possible as code (infrastructure as a code). Aim is to avoid manual work. Release to production should be safe and repeatable. Something like (varies across companies/industries) - developer pushes code, QA tests it in a QA environment, code goes to staging, then goes to production with a single click. Rollback is easy. Prod environment has monitoring so we know its state at any given time.

What is dev/qa/staging/prod? 
How can we achieve such separation of environments? From the developers’ (code) perspective - different configurations loaded per environment - e.g. via different configuration files or environmental variables
from DevOps perspective - using different processes/servers/data centers/cloud providers.

[Readlist](https://www.google.com/url?q=https://dev.to/pluralsight/the-top-10-books-on-devops-you-need-to-read-45m2&sa=D&ust=1573068867597000&usg=AFQjCNGvmIsf8ObOCltwRdTOKia9-6gdPA)


### ​1.2.2​ What is Agile, Scrum, Kanban, Waterfall
How does DevOps fit in the agile mindset - quick prototyping and deployment
- Waterfall - One long iteration to deliver the whole product. Requirements are gathered, the dev team implements them, then the QAs test the whole thing, then the product is shipped. Risky - difficult to predict ahead of time, since a waterfall is inherently lengthy - e.g. 1 year.  Would the product even be still relevant when it’s ready? What if half the team leaves halfway through. What if some technology on which you depend is discontinued. With waterfall, risk management is more difficult. 
- Scrum  ([diagram of the method](https://www.google.com/url?q=https://www.scrum.org/resources/what-is-scrum&sa=D&ust=1573068867596000&usg=AFQjCNGSD6R2HtL43wGhrm2Alzvm-M8gTw]))
#### Scrum 
* "Scrum replaces a programmed algorithmic approach with a heuristic one, with respect for people and self-organization to deal with unpredictability and solving complex problems." ([source](https://www.scrum.org/resources/what-is-scrum), accessed Aug, 2019) 
* A way to organize the efforts of a team so that a complex product/task can be delivered in a timely fashion.
* Product owner - knows what the customers and the other stakeholders want. Communicates this information to the teams that will actually deliver the software. The PO manages the product backlog which is a set of tasks.
* A subset of the tasks in the backlog is executed during a sprint. A sprint can be a week/two weeks/etc.
* Iterative approach. I.e. a shippable product should be the output of each sprint.
* DoD (definition of done) - the team is working on the tasks with the aim to deliver value to the end users. 
* The Focus is on the value given to the users. I.e. anything that doesn’t bring value is not prioritized.
* Daily scrum. The team discuss what they are doing, what help they need, etc.
* Scrum master - the person responsible for ensuring that scrum is properly executed within the organization. 
#### Agile 
Agile - a way to manage uncertainty. Umbrella term to accommodate different tactics and methodologies. Mindset of how to respond to changes and unexpected situations. Planning is done continuously - in accordance to new information.
#### Kanban
([sample kanban board](https://upload.wikimedia.org/wikipedia/commons/c/c2/Sample_Kanban_Board.png))
“Kanban is a popular framework used to implement agile software development. It requires real-time communication of capacity and full transparency of work. Work items are represented visually on a kanban board, allowing team members to see the state of every piece of work at any time.” ([source](https://www.atlassian.com/agile/kanban), accessed August, 2019)
From practical perspective, you have the kanban board with columns. Tasks go to these columns. Each column represents a state in which a task can be - e.g. To-do, in-progress, to be reviewed, staging, production/done.
​1.2.3​ Scripting foundation
What is scripting
it’s code that is written in a scripting language (bash, perl, etc.)
it’s code in the sense that we need to write it, but normally we don’t need to compile it (like we need to compile Java/C#/etc.)
typically, scripts are less complex than other software applications from software design perspective - e.g. they are shorter, smaller scope, no or simpler multithreading, classes, etc.
When do we use scripting
When we want to automate tasks that occur on some schedule
When we want to process data or react to an event
E.g. archive all application logs and upload them to an FTP server (or AWS S3)
Process all access logs and extract the IP and timestamp and forward them to the analytics team
Given a new git commit, build the application, zip it and upload it to application servers
text formats
we need a way to represent data - 
either application data such as a list of users that have used our site,
or as a way to declaratively represent some entity - e.g. write down a detailed representation of our servers that can be used to create them automatically with some tool - e.g. with AWS CloudFormation
YAML & JSON - popular these days. XML somewhat obsolete. They each have their own syntax and official specifications. Programming languages then provide libraries that implement the specification.
YAML
clean syntax, language libraries have support for parsing it
JSON
more verbose
variable types (e.g. represent different types of data) - number, boolean, string, lists, mappings
​1.2.4​ Bash
If you are dealing with Linux servers - you must have at least a basic understanding of the syntax and semantics of bash
Why is it handy - knowing bash will make your life as a DevOps easier and more pleasant. It’s a huge beast but you don’t need to understand it all to be productive with it. It’s used in Linux servers - and we use Linux servers everywhere. The software that we operate runs on Linux. Our devops automation tasks also use it. Linux is on cloud instances, bare metal servers, Windows WSL, Docker, even the AWS Serverless Lambda runs on a Linux container under the hood. Understanding the execution environment of the software that you operate is invaluable. 
What is bash
Why use it - automation of various tasks.
Interactive vs non-interactive shell
interactive shell - when we type commands and get output
non-interactive - when we run a shell script it runs in its own process
day-to-day commands 
Linux distributions come with a set of built-in commands that we can use. We can use these commands in an interactive shell (or in our scripts). These commands can do file or network I/O and others. They do one thing but they do it well. We can compose commands (pipe them) - the output of one command goes as an input to the next command. We can build powerful pipelines this way with little code.
pwd, cd, ls, cat, touch, mkdir, echo, grep, sed, apt, ping, nslookup, whereis, watch, less, find, curl, free, df/du, ps
pipes
globbing
linux -  directory structure and conventions
Cron gotchas
basic cron idea
execute tasks (scripts, programs) on a schedule
basic syntax is with * * * * *
also possible to use e.g. /5 * * * *- every five minutes
where to put them
via `crontab -e [-u <user>]`
/etc/cron.d
/etc/cron.[daily|weekly|monthly]
view existing ones
crontab -l 
sudo crontab -l -u root
edit via `crontab -e` or placing files in /etc/cron.d/
gotcha with environment variables - limited set of environment variables are passed to the program that cron will execute
environment variables
variables that you can define in the context of the operation system.
applications that you start have access to those variables
the app can change their behaviour based on the values of the environmental variables - e.g. load the QA config if APP_ENV=qa and the Prod one if APP_ENV=prod
very handy because env vars are widely adopted - you can set them in your shell, so that processes you start have access to them, you can set them in your IDE so that when you test on your machine the code has appropriate env vars, you can pass them to docker containers
.bash_profile (.profile) - in the home directory of users. Per user configs, env vars
Writing bash scripts
redirect stdout to a file
return codes semantics
if a script finishes successfully, by convention, its return code is 0. 0 means success
Non-zero values indicate that there was an error
bash scripting
stdout & stderr and redirection
example
shebang
file permissions - users, groups, chown, chmod
supervisord
logrotate
Ctrl-R
search in the previously invoked commands in an interactive shell
command-completion - tab :)
aliases	
example with simplistic update of a site
conf.d convention
when using some linux packages (e.g. logrotate, supervisord, cron, etc.), you need a configuration file that contains your settings. Often, we need multiple such files. There’s a convention with folders ending with .d - if you put files there, they will all be considered by the software that you configure
​1.2.5​ Git	

Git is a version control system. Why do we care about git?
We use git to collaborate with the rest of our team on files (files can be code - Python scripts, infrastructure-as-a-code templates, Java code, etc.). 
The application developers use git too. On each commit we might want to trigger a whole build and deploy pipeline that we, as a DevOps, must set up. We need to have a working understanding of git to do that 
git gives a shared repository that we can use to store our code and make changes to it, whilst collaborating with other people without risk of losing work. I.e. multiple people can work on the same codebase at the same time, without risk of losing work
How does git work and source control intro
“To be efficient, if the files have not changed, Git doesn’t store the file again—just a link to the previous identical file it has already stored.”
Git has three main states that your files can reside in: modified, staged and committed
Committed means that the data is safely stored in your local database. Modified means that you have changed the file but have not committed it to your database yet. Staged means that you have marked a modified file to go into your next commit 
common workflow
scenario 1
You join a team of developers that collaborate on the codebase of their project 
There’s a bug in the code that you need to fix
There’s a single, “main” code repository that the team has agreed to use (i.e. “origin”). It’s typically hosted on a git web service like GitHub, BitBucket, CodeCommit where a copy of the project’s code is held. Developers sync their changes to this origin repository. It acts as a single source of truth.
Given the remote code repository containing the project codebase, you clone it locally to your computer in a folder
You now see the project contents - e.g. source code files, images, etc. directly on your filesystem
There’s also a .git directory within the local project directory which holds Git’s internal database and settings
You make some changes to the source code - e.g. fix the bug
Using a command you stage the file(s) you’ve changed  - staging the files puts them together in the staging area of git, ready to be committed
Given you have file(s) in the staging area, you can commit them
A commit is a logically grouped set of changes - e.g. a commit with file changes that fixes some bug. A commit, from our perspective, consists of the changes to file(s), a descriptive message which explains the changes, author and a timestamp. 
Once you commit your changes, they are stored in the local git database and become part of the project’s history. 
You want to share your work with the rest of the team, so you push your changes (the commit) to the origin repository
For your teammates to see your work, from their own computers they should pull from the remote origin repository. After they pull, the changes from your commit, will be applied on their filesystem too
(demo)
scenario 2
You are a solo developer and you’re working on a new project
You’ve pushed some commits already 
By default, when using git - there’s a single “stream” of commits - the master branch. You start from an empty repository, you add files, you commit every now and then and your commits are applied on the master branch. It’s a linear history of commits.
However, a powerful concept of git is branching. You can branch out from the default, master, branch to a different branch. Once on the new branch, when you commit, your commits are applied on this branch
This is useful if you want to work on an experimental feature, continuing from your existing work, but without cluttering your “master” branch which has a working version of the project. Working on a new branch enables you to keep your master history clean, while you are working on the new feature. When on a new branch, you can still commit to it.
If you are happy with the new feature, you can merge the new branch into master. This will apply all commits from the new branch to the master branch. If you are unhappy with the new feature, you can just discard the new branch and switch back to master.
Git for DevOps
In the context of DevOps, we care about git because most of the times the application’s code is hosted via git (or a similar tool). 
When a developer pushes a commit to the origin repository, this can trigger our deployment pipeline. The pipeline is triggered by the commit, then some service can fetch the newest application’s code. Then the code can be built and eventually uploaded to the application’s servers
The above is a simplified example. We can run tests on the new version of the app, we can perform static analysis of the code and reject the commit if the code doesn’t comply with some predefined quality (e.g. too lengthy methods, not enough documentation, etc.). We can send a Slack message to the QA team when the new version gets deployed to the QA environment. With some Python/Bash the possibilities are endless.
Practical
You can use git on all popular platforms (Linux, Windows, MacOS). 
Be cautious about line endings (there’s a different standard for Linux and Windows). Git has a setting that lets you develop with whatever line ending you want, but when you commit, text files are converted to \n.
You can use git through the CLI (windows cmd, linux bash shell) or via a GUI - a popular one is SourceTree. Most IDEs have git integration - e.g. PyCharm, Visual Studio (Code). 
Personal opinion - good idea to start out with the CLI to get a feeling of git and then move to a GUI if you need.
​1.3​ Lecture 2
Python
Python 2 vs  python 3
If you can, use Python 3. Support for Python 2 will stop in a couple of months, Python 3.0 is 11 years old.
Considerations
Not the fastest language around. Think how much you care about this. Python is fast to write. 
Duck typing. If you don’t have a background in programming, the way Python handles typing can be actually easier to understand.
standard library
variables, functions, if-else, for-loop, exceptions
split strings, dictionaries
parsing command line arguments
reading env vars
file IO & requests library
pip
a tool to manage 3rd party packages  that we use in our code
how to install it
download the get-pip.py file and then run it with via python
install & freeze commands
`pip install boto3` to install the newest boto3 version
`pip install boto3==1.9.219` - install a specific version
`pip freeze` - show the installed packages in the current environment
convention - put your code’s required packages in the the requirements.txt file
pycharm
new project
run configurations
debugger
good to know (google it)
modules and packages
error handling with exceptions in python
virtualenv and pipenv
