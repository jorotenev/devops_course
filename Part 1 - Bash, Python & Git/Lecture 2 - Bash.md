# Lecture 2 - Bash
## Scripting foundation

### What is scripting
Script - it’s code that is written in a scripting language such as bash, perl, etc.
It’s code in the sense that we need to write it, but normally we don’t need to compile manually it (like we need to compile Java/C/C#/etc.)
__Typically__, scripts are less complex than other software applications from software design perspective - e.g. they tend to be shorter, with smaller scope, no or simpler multithreading, classes, etc.
### When do we use scripting
* When we want to automate tasks that occur on some schedule
* When we want to process data or react to an event
* E.g. archive all application logs and upload them to an FTP server (or AWS S3)
* Process all access logs and extract the IP and timestamp and forward them to the analytics team
* Given a new git commit, build the application, zip it and upload it to application servers
## Text Formats
We need a way to represent data -  either application data such as a list of users that have used our site, or as a way to declaratively represent some entity - e.g. write down a detailed representation of our servers that can be used to create them automatically with some tool - e.g. with AWS CloudFormation. 

YAML & JSON - popular these days. XML somewhat obsolete. They each have their own syntax and official specifications. Programming languages then provide libraries that implement the specification so that it's easier to read and write data in a format like YAML/JSON/XML.
*  YAML
    * clean syntax, language libraries have support for parsing it
* JSON
    * more verbose
The text formats support different __variable types__ (e.g. represent different types of data) - number, boolean, string, lists, mappings.
​
# Bash
If you are dealing with Linux servers - you __must__ have at least a basic understanding of the syntax and semantics of Bash

* Why is it handy - knowing Bash will make your life as a DevOps easier and more pleasant. It’s a huge beast but you don’t need to understand it all to be productive with it. It’s used in Linux servers - and we use Linux servers everywhere. The software that we operate runs on Linux. Our DevOps automation tasks also use it. Linux is on cloud instances, bare metal servers, Windows WSL, Docker, even the AWS Serverless Lambda runs on a Linux container under the hood. Understanding the execution environment of the software that you operate is invaluable. 
## What is bash
* Why use it - automation of various tasks.
* [Interactive vs non-interactive shell](https://unix.stackexchange.com/questions/43385/what-do-you-mean-by-interactive-shell)
* [interactive shell](https://imgur.com/3X3TB1t) - when we type commands and get output
* [non-interactive](https://imgur.com/SvXx9EW) - when we run a shell script it runs in its own process
### Day-to-day commands 
* [Gist with commands with examples](https://gist.github.com/jorotenev/ef2c84860fb7df87c2bcb7737bf9ffad#file-linux-commands-sh)
* Linux distributions come with a set of built-in commands. We can use these commands in an interactive shell (or in our scripts). These commands can do file or network I/O and others. The philosophy behind these commands is that they do one thing but they do it well. We can compose commands (pipe them) - the output of one command goes as an input to the next command. We can build powerful pipelines this way with little code.
* pwd, cd, ls, cat, touch, mkdir, echo, grep, sed, apt, ping, nslookup, whereis, watch, less, find, curl, free, df/du, ps
* [pipes](https://www.google.com/url?q=https://ryanstutorials.net/linuxtutorial/piping.php&sa=D&ust=1573068867579000&usg=AFQjCNH9mbHvyyHYaq22jS7CEHfisjM0zQ)
* globbing
 * [Linux directory structure and conventions](https://imgur.com/GncnnQA)
* Cron gotchas
* basic cron idea -  execute tasks (scripts, programs) on a schedule
* basic syntax is `<schedule> <cmd>` - e.g. `1 * * * * echo hi >> /var/log/sample.log` - will run the command `echo hi >> /var/log/sample.log` every on the first minute (minute 1), every hour, every day, every month, every year.
also possible to use e.g. /5 * * * *- every five minutes
* very handy cron "calulactor" - [link](https://crontab.guru/#5_1_*_*_1)
* where to put cron tasks
    * via the `crontab -e [-u <user>]` command
    * in a file in `/etc/cron.d/`
    * in a file in the following dirs `/etc/cron.[daily|weekly|monthly]`
* To view existing cron tasks, added via `crontab -e`
    * for the current user `crontab -l`
    * for other users `sudo crontab -l -u root`

* NB! When using cron, be aware of the environmental variables which the scripts being execute within the cron tasks need. Limited set of environment variables are passed to the program that cron will execute - i.e. different from what you'd see from running, say, the `env` command.
## Environment variables
* Variables that you can define in the context of the operation system.  
* Applications that you start can have access to these variables.  
* The app can change their behaviour based on the values of the environmental variables - e.g. load the QA config if APP_ENV=qa and the Prod one if APP_ENV=prod
* Very handy because env vars are widely adopted - you can set them in your shell, so that processes you start have access to them, you can set them in your IDE so that when you test on your machine the code has appropriate env vars, you can pass them to docker containers, etc. etc.
## Writing bash scripts
* [Gist with samples](https://gist.github.com/jorotenev/ef2c84860fb7df87c2bcb7737bf9ffad#file-bash-example-sh)
* redirect stdout to a file
* semantics of return codes of scripts 
    * if a script finishes successfully, by convention, its return code is 0. 0 means success
    * Non-zero values indicate that there was an error
* stdout & stderr and redirection
    * [example](https://gist.github.com/jorotenev/ef2c84860fb7df87c2bcb7737bf9ffad#file-bash-stdout-stderr-sh)
* shebang
* file permissions - users, groups, chown, chmod

* [supervisord](http://supervisord.org/configuration.html)
    * if you have some process (e.g. some worker script) that you want to ensure is always working, you can launch it via supervisord which will ensure that your process is always running and will relaunch it in case your program exits for some reason. 
* [logrotate](https://www.thegeekstuff.com/2010/07/logrotate-examples/)
    * production servers accumulate a lot of logs. This can become problematic because log files take up disk space. Thus, we need to __rotate__ files - i.e. archive log files every now and then (based on file age or size). Logrotate automates this for us
* Ctrl-R - can search in the history of the commands you've invoked in an interactive shell (tested on ubuntu)

* command-completion - tab :)
* command aliase - can write shorter synonyms of long commands.
    * [alias example with a function](https://gist.github.com/jorotenev/ef2c84860fb7df87c2bcb7737bf9ffad#file-bash_aliases)
* conf.d convention
    * when using some linux packages (e.g. logrotate, supervisord, cron, etc.), you might need a configuration file that contains your settings. Often, we need multiple such files. There’s a convention with folders ending with .d - if you put files there, they will all be considered by the software that you configure
