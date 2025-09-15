#File: homework1.py
# ---- Variables and Data Types --- #
a=10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a real number that has a decimal

c=3j
print(c)
print(type(c)) #c is a complex number, a number that has both a real and an imaginary part

d= "hello"
print(d)
print(type(d)) #d is a string, or characters enclosed in quotes which represent textual data

e = [1,2,3]
print(e)
print(type(e)) #e is a list, or a mutable (changeable) and ordered collection of items. In this case, a collection of intengers.

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) #f is a dictionary, or an unordered collection of key-value (identifier and its associated data) pairs

g = (1,2)
print(g)
print(type(g)) #g is a tuple, or an ordered and immutable (unchangeable) collection of items

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) #h is a list, or a mutable (changeable) and ordered colelction of items. In this case, a collection of strings.

i = True
print(i)
print(type(i)) #i is a boolean, a value which can be either "True" or "False"

j= None
print(j)
print(type(j)) #j is a NoneType, a value that represents the absence of data

k= [True, "blue", 12] 
print(k)
print(type(k)) #k is a list, or a mutable (changeable) and ordered collection of items. In this case, the list contains multiple data types. 

l = str(14)
print(l)
print(type(l)) #l is the str() function, which converts values into string equivalents

m = 1e4
print(m)
print(type(m)) #m is a float value, expressed in scientific notation; 1e4 means 10 raised to the power of four. 

# Questions:
# 1. I found nine different data types
# 2. Integer, String, Float, Complex Number, NoneType, List, Tuple, Dictionary, Boolean
# 3. b,m are floats; e,h,k are lists; l,d are strings
# 4. l is a string; it is not an intenger becasuese the str() function converts values of any datatype into their string equivalent
# 5. see below
n = {1,3,4,2}
print(n)
print(type(n)) #n is a set, an unordered collection of unique values; duplicate values cannot be added to a set.

# ---- Booleans --- #
print(10 > 9) #True, 10 is greater than 9
print(10 == 9) #False, 10 is not equal to 9
print(10 <= 9) #False, 10 is not less than or equal to 9
print(bool("abc")) #True, abc is a non-empty string so it is true
print(bool(123)) #True, 123 is a non-zero integer so it is true
print(bool(["apple", "cherry", "banana"])) #True, "apple", "cherry", "banana" is a non empty list, so it is true
print(bool(True)) #True, True is already a boolean value so it is returned as true
print(bool(False)) #False, False is already a boolean value so it is returned as false
print(bool(0)) #False, zero is an intenger that is returned as false
print(bool("")) #False, it is an empty string that is returned as false
print(bool(" ")) #True, it is a non-empty string that is returned as true 
print(bool(())) #False, it is an empty tuple that is returned as false
print(bool([])) #False, it is an empty list, so it is returned as false
print(bool({})) #False, it is an empty dictionary, so it is returned as false
print(bool(True and False)) #False, True and False is false
print(bool(True and True)) #True, True and True is true
print(bool(False and False)) #False, False and False is false
print(bool(True or False)) #True, True or False is true
print(bool(True or True)) #True, True or True is true
print(bool(False or False)) #False, False or False is false
print(bool(not(False))) #True, not False is true
print(bool(not(True))) #False, not True is false

#Questions:
#1. I notice that empty values (like an empty list) return as False, while non-empty values return as True. Of course, statements that cannot be true (like something being True and False at the same time) are returned as false. 
#2. At first I was surprised that True or False returned as True- but I think because that statement is necessarily false, it makes sense to return as true?
#3. 5<10 will return as True, since five is less than ten
#4. 10<5 will return as False, since ten is greater than five

# ---- Operators --- #

#Arithemetic
print(10+5) #15, performs addition
print(10-5) #5, performs subtraction
print(2*4) #8, performs multiplication
print(6/3) #2.0, performs division
print(5%2) #1, returns the remainder after performing division
print(3**2) #9, performs an exponent
print(15//2) #7, performs division and rounds down to nearest whole number

#Comparison
print(5 == 2) #False, evaluates whether the values are equivalent
print(10 != 10) #False, evaluates whether the values are not equivalent
print(2<5) #True, evaluates whether the less than comparison is true or not
print(12>5) #True, evaluates whether the greater than comparison is true or not
print(5 <= 6) #True, evaluates whether the less than or equal to comparison is true or not
print(1 >= 10) #False, evaluates whether the greater than or equal to comparison is true or not

#Assignments
x = 5

x +=5
print(x) #10, Adds five to the variable and assigns that new value to it

x -= 4
print(x) #6, Subtracts four from the variable and assigns that new value to it

x *= 3
print(x) #18, Multiplies the variable by three and assigns the new value to it

#Logical
#1. the operator "and" ensures that an expression can only be evaluated as true if all parts of it are true. 
# For example: print(3>2 and 2>1) will evaluate as True, while print(3>2 and 1>2 ) will evaluate as False
#2. the operator "or" ensures that an expression can be evaluated as true if at least one of the parts of it are true. 
# For example: print(3>2 or 2<1) will evaluate as True, while print(2>3 or 2<1) will evaluate as false
#3. Using the "not" operator will evaluate to the oppsoite value of the expression.
# For example: print(not (3>2 and 2<1)) will evaluate as True, while print(not (3>2 and 2>1)) will evaluate as False

#More Questions
#1. / will perform division and return a decimal value, while // performs division but rounds down to the nearest whole number.
#2. % will perform division and return the remainder, while // will simply round down the decimal value answer (if there is one
#3. I would use % to calculuate the remainder of a division. For example print(10%3) will return 1, since the remainder of 10/3 is 1. 
#4. Assignment operators will assign the value on the right side of the operator to teh variable on the left side. This can be a simply "=", or it can contian an operation that will change the initial value of the variable.

# --- Strings ---#
my_string = "hello"

print(my_string) #Prints: hello
print(my_string[0]) #Prints: the first letter in hello (h)
print(my_string[1]) #Prints: the second letter in hello (e)
print(my_string[2]) #Prints the third letter in hello (l)
print(my_string[3]) #Prints the fourth letter in hello (l)
print(my_string[4]) #Prints the fifth letter in hello (o)
print(my_string[-1]) #Prints the last letter in hello (o)
print(my_string[1:3]) #Prints the second letter of hello, and prints every letter until (but not including) the fourth letter of hello
print(my_string[0:5:2]) #Prints the first letter of hello, and prints every two letters until (but not including) the sixth letter
print(len(my_string)) #Prints 5, the length of the word hello
print(my_string + "goodbye") #Prints hellogoodbye (combining the strings)
print(my_string*7) #Prints hellohellohellohellohellohellohello, which is my_string seven tiems

#Questions
#1. Slicing in python helps us return a portion or "slice" of a sequence like a string- this portion can be a single element or a range of elements. Manipulations 2-9 all involved splicing. 
#2. see below
name = "Oski"
print("Hello, my name is", name) #Prints Hello, my name is Oski

#3. see below
name = "Oski"
print(f"Hello, my name is {name}") #Prints Hello, my name is Oski

#4. The first print statement puts the name variable after the string, while the second statement embeds the name variable within the string. 
#This is because the second print statement is an f-string, which is a string that allows us to embed python code within the string

#---Terminal Commands---#
#1. cd
# Change Directory- move from one folder to another
# Example: cd python_decal_fa25

#2. ls
# Lists Files- used to list all the contents of a folder
# Example: ls jeevika

#3. ls -a
# lists all files- used to list all contents of a folder, including hidden files and folders
# Example: ls -a jeevika

#4. mkdir
# Make directory- creates a new folder
# Example: mkdir new_folder

#5. cat
# Displays the contents of a file
# Example: cat test.py

#6. pwd
# Print working directory- shows the full path from the root directory to your current directory
# Example: type "pwd" within any folder and you will get the full path from the root directory to that folder

#7. cd .. 
# .. refers to the parent directory of your current folder. So, cd .. is used to move up one directory level
# Example: cd .. within "jeevika" to move to "python_decal_fa25"

#8. cd . 
# . refers to the current directory. The commands specifies to stay in the current directory.
# Example: type "cd ." within "python_decal_fa25" to stay in the folder

#9. cd ~
# This command moves you to the home directory- /Users/username
# Example: If I type cd ~ on my terminal, I would end up in my home directory /Users/jeevika

#10. cp
# This command will copy a file or directory
# Example: cp test.py

#11. mv
# Allows you to move or rename files or directories
# Example: to move a file: mv /Users/jeevikarajasekar/python_decal_fa25/jeevika/test.py.save /Users/jeevikarajasekar/python_decal_fa25/  
#          to rename a file: mv test.py.save new_file_name

#12.rm 
# Allows you to remove files or folders
# Example: rm new_file_name will delete new_file_name

#13.clear
# Clears the terminal screen
# Example: simply type clear

#14.grep
# Searches for patterns/matching lines within a file, and then prints them
# Example: grep "print(5+5)" test.py 

#Questions
#1. rmdir- used to remove an empty file or directory- Example: Simply type rmdir folder_name to remove the empty folder called folder_name 
# history- displays command history- Example: simply type history into the command line to get a display of all the commands you have inputted so far. 
# touch- creates an empty file- Example: simply type touch followed by the name of the file you want to create.

#2. ls will list the contents of a folder, while ls -a lists content as well as hidden files and folders. These hidden files usually contain critical data that should not be modified, so they are not displayed by the ls command. 

#3. As stated above, a hidden file is one that is not typically displayed in a directory because it may contain critical information that should not be modified. 

#4. cp -i will prompt you before accidentally overwriting an existing file during the copy. type cp -i instead of just cp.
# ls -l will list contents with permissions, the owner of the file, the file size, and the date of modificiation. type ls -l instead of just ls
#  grep -i will perform a case-insensitive search for the pattern. type grep -i intstead of just grep.



