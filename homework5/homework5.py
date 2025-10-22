#Homework 5

# --- Homeowrk 1+2 Review --- #

#Vocab Review#
#1 Git - a version control system that runs locally to track changes to files. 
# Github- a place to store git repositories on the internet, allowing for colloboration. 

#2 Terminal- a window that allows the user to interact directly with their computer and have it execute their commands. 
# Command Line- The actual interface in which users type the commands within the terminal. 

#3 Local Repository- stores the version history and committed changes of a project within the local computer. All work is offline and not viewable by collaborators. 
# Remote Repository- stores project history on the cloud, where multiple people can collaborate on the project together. Commited changes in local respositories are pushed onto remote respositories. 

#4 Version Control - The tracking of a changes to a project file over time. It stores all versions/history of the project. These versions are stored in a repository. 

#5 Staging area- an intermediate location where changes to a file are prepared to be committed to the repository. This is where changes are stored after the "git add" command is executed.

#6 Git add- after executing this command, changes tracked by git will be stored in the staging area. 

#7 Git commit- after executing this comand, changes in the staging area will be committed to the local repository.

#8 git push- after executing this command, changes commited to the local repository will be pushed to the cloud. (for example, to a remote repository like github)

#9 git status - displays the status of the working directory, including changes that have been made since the last commit. 

#10 git pull - pulls files and changes from a remote repository into your local repository. 

#11 pwd- displays the full pathway from your home directory to your current working directory.

#12 ls - lists all visible files that are in your current working directory. 

#13 cd - used to change your current working directory into another one. 

#14 nano- used to create and/or edit a file with a text editor within the terminal. 

#15 touch- used to create new files while in the terminal. 

#16 mv - used to move files/directories from one directory to another. Can also rename files or directories. 

#17 rm - used to remove files/directories. 

#18 cat- displays the contents of a file within the terminal. 

#A Directory Tree#

#1 The pwd command will tell me my current working directory and the pathway to it. 
#2 The ls command will list all files in the working directory. 
#3 in this order: cd .., cd brianna_repo, git pull
#4 mv homework.py ~/python_decal/judy_decal/homework/
#5 cd .., cd judy_decal, cd homework
#6 cat homework.py would display the contents of homework.py.
#7 git add, git commit -m "message", git push origin main
#8 it seems like the remote repository Judy is pushing to has some changes from a different repository. Judy should use the git pull command to integrate these changes with ther local repository before pushing the changes again. 
#9 absolute path: ~/Recents/ but to get to recents (relative path): ../../../Recents

#Draw Your Directory Tree#
#see the screenshot

# --- Homework 3 Review ---#
#Data Types#
def checkDataType(data):
    return f"{type(data)}"
    
#Conditionals#
def evenOrOdd(intenger):
    if intenger%2 == 0:
        print("Even")
    else:
        print("Odd")
    return

#--- Loops ---#
numbers = []

def sumWithLoop(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

# --- Homework 4 Review ---#
#Lists#
def duplicateList(list):
    new_list = []
    for i in list:
        new_list.append(i) 
        new_list.append(i)
    return new_list

#Debugging#
def square(num):
    return num * num
#a colon must be included after def square(num)

# --- Running Your Code ---#
#printing favorite function:
print(duplicateList(["I", "am", "sleeping", "early", "today", "!"]))
