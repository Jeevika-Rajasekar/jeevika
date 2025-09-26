# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
#Git is a "version control system" which tracks changes made to files/tracks versions of a file. It allows multiple users to work on the same file, and all changes are stored in a local respository. 
#Git Hub is an internet service that stores Git respositories in the cloud, allowing for colloboration and sharing.
#Git Bash allows Windows users to use the Bash shell (which isn't native to Windows systems), allowing them to use git commands in their terminal. 

# 2) What’s the difference between the terminal and the command line?
#The terminal is a system which allows the user to interact with the operating system of their computer by inputting commands. 
#The command line is the line in the terminal where you enter commands.

# 3) How does Windows PowerShell differ from Git Bash?
#Git Bash uses different command syntax from Powershell. Git Bash is geared towards interacting with Git repositories and using Git commands while Powershell is geared towards interaction with Windows system administration. 

# 4) What’s the difference between Anaconda, conda, and Python?
#Anaconda is a group of Python packages that are useful for data science. Conda is a package manager, embedded in the Anaconda system, that manages things like the installation of packages. Python is the programming language itself, and it is the language that Anaconda packages are written in.

# 5) What is VS Code? 
#VS code, or Visual Studio Code, is a code editor that is useful for the actual writing and debugging of code. 
 
# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
#Jupyter Notebook is a place where we can write code in interactive "cells" and run that code within a single document. Jupyterlab is an expansion of Jupyter Notebook that allows us to manage multiple notebooks side by side, and has other additional features. 

# 7) What does ~/ mean?
#~/ represents the home directory of the file system that is being worked in. 

# 8) What’s the difference between an absolute path and a relative path?
# The absolute path is the full path from the root directory to the target file or directory, while the relative path is the path from the current working directory to the target file or directory. 

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
#absolute: ~/python_decal_fa25/course_assignments/homework2
#relative: ../course_assignments/homework2

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
#cd.. lets you move one level up in your directories. 

# 11) What would rm ./ do in your current directory? (Don’t try it!)
#rm ./ would delete my current directory, since ./ refers to my current directory. 

# 12) What do the following commands do?
# git add- this commands adds the new changes you've made to your working directory to a "staging area"
# git commit- this command locally saves all the changes you have added to the staging area. 
# git push- this command saves all the changes remotely in git hub. 

# 13) What's the difference between "git add ." and "git add <file>"?
# "git add ." would prepare to save all the changes you've made to your current working directory, while "git add <file>" would prepare to save all changes made to the specified file. 

# 14) What do "git status" and "git log -1" do?
#calling "git status" will display information about the status of your current working directory, such as the files that have been added to the staging area or unsaved changes that have not yet been added to the staging area. 
#calling git log -1 will show you the most recent commit you have made to the Git repository.
 

# 15) What’s the difference between cloning a repository and pulling from it?
#cloning will create a local copy of an entire remote repository. pulling from the remote repository will simply update your local repository with changes made in the remote repository.  

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
#To be honest I don't think I have done enough coding yet to have a super frustrating bug... I guess besides forgetting to put a colon every now and then. I troubleshoot by shaking myself awake and realizing my mistake. 

# 17) What’s a question you still have? What’s something you’re confused about?
#How does one keep all these commands in their head? Do most people who code have all this memorized, or is it normal to have to consult resources all the time? 

# 18) Tell me a fun fact!
#I used to play a silly 2d space agency game on my phone, and I timed it just right so that I could land on the moon for the first time on the 50th anniversary of the actual moon landing (July 20th 2019). Best day of my life. I guess that's a fact?

# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)
print(50%4)
#this will divide 50 by 4, and return the remainder (which would be 2 in this case). I just really like remainders. 
