# Git	
* Git is a version control system. 
* We use git to collaborate with the rest of our team on files (files can be code - Python scripts, infrastructure-as-a-code templates, Java code, etc.). 
* The application developers use git too. On each commit we might want to trigger a whole build and deploy pipeline that we, as a DevOps, must set up. We need to have a working understanding of git to do that 
* git gives a shared repository that we can use to store our code and make changes to it, whilst collaborating with other people without risk of losing work. I.e. multiple people can work on the same codebase at the same time, without risk of losing work 
* [How does git work](https://git-scm.com/book/en/v1/Getting-Started-Git-Basics) and [source control intro](https://git-scm.com/book/en/v1/Getting-Started-About-Version-Control)
* Git has three main states that your files can reside in: modified, staged and committed
* "Committed means that the data is safely stored in your local database. Modified means that you have changed the file but have not committed it to your database yet. Staged means that you have marked a modified file to go into your next commit" ([source](https://git-scm.com/book/eo/v1/Ekkomenci-Git-Basics), accessed Aug, 2019) 
# Common Workflow
## Scenario 1 - simple use case
* You join a team of developers that collaborate on the codebase of their project 
* There’s a bug in the code that you need to fix
* There’s a single, “main” code repository that the team has agreed to use (i.e. “origin”). It’s typically hosted on a git web service like GitHub, BitBucket or CodeCommit where a copy of the project’s code is held. Developers sync their changes to this origin repository. It acts as a single source of truth.
* Given the remote code repository containing the project codebase, you clone it locally to your computer in a folder
* You now see the project contents - e.g. source code files, images, etc. directly on your filesystem
* There’s also a .git directory within the local project directory which holds Git’s internal database and settings
* You make some changes to the source code - e.g. fix the bug
* Using a command you stage the file(s) you’ve changed  - staging the files puts them together in the staging area of git, ready to be committed
* Given you have file(s) in the staging area, you can commit them
* A commit is a logically grouped set of changes - e.g. a commit with file changes that fixes some bug. A commit, from our perspective, consists of the changes to file(s), a descriptive message which explains the changes, author and a timestamp. 
* Once you commit your changes, they are stored in the local git database and become part of the project’s history. 
* You want to share your work with the rest of the team, so you push your changes (the commit) to the origin repository
* For your teammates to see your work, from their own computers they should pull from the remote origin repository. After they pull, the changes from your commit, will be applied on their filesystem too
* [demo](https://gist.github.com/jorotenev/ef2c84860fb7df87c2bcb7737bf9ffad#file-git-demo-sh)
## Scenario 2 - branches
* You are a solo developer and you’re working on a new project
* You’ve pushed some commits already 
* By default, when using git - there’s a single “stream” of commits - the master branch. You start from an empty repository, you add files, you commit every now and then and your commits are applied on the master branch. It’s a linear history of commits.
* However, a powerful concept of git is branching. You can branch out from the default, master, branch to a different branch. Once on the new branch, when you commit, your commits are applied on this branch
* This is useful if you want to work on an experimental feature, continuing from your existing work, but without cluttering your “master” branch which has a working version of the project. Working on a new branch enables you to keep your master history clean, while you are working on the new feature. When on a new branch, you can still commit to it.
* If you are happy with the new feature, you can merge the new branch into master. * * This will apply all commits from the new branch to the master branch. If you are unhappy with the new feature, you can just discard the new branch and switch back to master.

# Git for DevOps
* In the context of DevOps, we care about git because most of the times the application’s code is hosted via git (or some other VCS system). 
* When a developer pushes a commit to the origin repository, this can trigger our deployment pipeline. The pipeline is triggered by the commit, then some service can fetch the newest application’s code. Then the code can be built and eventually uploaded to the application’s servers
* The above is a simplified example. We can run tests on the new version of the app, we can perform static analysis of the code and reject the commit if the code doesn’t comply with some predefined quality (e.g. too lengthy methods, not enough documentation, etc.). We can send a Slack message to the QA team when the new version gets deployed to the QA environment. With some Python/Bash the possibilities are endless.
## Practical
* You can use git on all popular platforms (Linux, Windows, MacOS). 
* Be cautious about line endings (there’s a different standard for Linux and Windows). Git has a setting that lets you develop with whatever line ending you want, but when you commit, text files are converted to \n.
* You can use git through the CLI (windows cmd, linux bash shell) or via a GUI - a popular one is SourceTree. Most IDEs have git integration - e.g. PyCharm, Visual Studio (Code). 
* Personal opinion - good idea to start out with the CLI to get a feeling of git and then move to a GUI if you need.
