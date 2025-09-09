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
print(bool(" ")) #True, it is a non-empty string that is retruned as true 
print(bool(())) #
