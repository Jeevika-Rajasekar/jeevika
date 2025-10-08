#--- Print Functions ---#

def say_goodbye(name): 
	print("Goodbye", name) #says goodbye

def area_of_circle(radius):
	print(2*3.14*radius) #calculates area of circle based on radius

#--- Return Functions ---#

def subtract(a,b): 
	return a - b #subtracts b from a 

def multiply(a,b):
	return a * b #multiplies a and b

def divide(a,b):
	return a/b #divides b from a

#--- Conditionals ---#

def max_min_temps(temps):
	return(min(temps), max(temps)) #returns the maximum and minimun temperatures from a list of temperature readings

def weekend_checker(day_of_week): #returns whether or not is a weekend based on an intenger representing a day of the week (where Monday = 1 and Sunday = 7) 
	if day_of_week > 5:
		return True
	else:
		return False 

def fuel_efficiency(distance,fuel_used): # returns fuel_efficiency based on distance and fuel used.
	return distance/fuel_used

def encryption(data): #encrypts my very important data by moving the last digit of an intenger to the front of the intenger
	return f"{data%10}" + f"{data//10}"

#--- Loops ---#
def powers(x,y): #takes x to the power of y without ** or pow()
	initial_value= x
	for i in range(1,y):
		x=x*initial_value
	return(x)

def minimum(integers): #finds the minimum with a for loop
	min= integers[0]
	for i in integers:
		if i < min:
			min = i
	return min

def maximum(integers): #finds the maximum with a for loop
	max = integers[0]
	for i in integers:
		if i > max:
			max = i
	return max

def minimum_2(integers): #finds the minimum with a while loop
	min_2 = integers[0]
	i = 0	
	while i < len(integers):
		if integers[i] < min_2:
			min_2 = integers[i]
		i += 1
	return min_2

def maximum_2(integers): #finds the maximum with a while loop
	max_2 = integers[0]
	i = 0
	while i < len(integers):
		if integers[i] > max_2:
			max_2 = integers[i]
		i+=1
	return max_2

def sum_of_digits(integer):
	list_of_digits= [int(i) for i in str(integer)] #converts the intenger to a string and then into a list of digits
	sum = 0
	for i in list_of_digits:
		sum += i
	return sum

#--- Running Your Script ---#

#from "Secret Code"
data = 24011984

result = encryption(data) #moves the last digit to the front of the intenger

print(f"The result of Secret Code (5.4) with data = {24011984} is {result}")
	  