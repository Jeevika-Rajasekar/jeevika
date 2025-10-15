# Homework 4 

# ---- Lists ---- #

#Operations
favorite_foods = ["rice", "noodles", "cake", "milk", "cheese" ]

#1
print(favorite_foods[1])
#2
print(favorite_foods[-1])
#3
favorite_foods.append("dosa")
#4
favorite_foods.insert(0,"apple")
#5
del(favorite_foods[2])
#6
print(len(favorite_foods))
#7
for food in favorite_foods:
    print(food.upper()) # ERROR I encountered this error: "AttributeError: 'list' object has no attribute 'upper'". I originally wrote print(favorite_foods.upper()), but changed it to print(foods.upper()), since we can only make the individual strings upper case. 
#8
new_favorite_foods= [favorite_foods[0:5:5]] # ERROR I encountered this error: "TypeError: list indices must be integers or slices, not tuple". I originally wrote new_favorite_foods= [favorite_foods[0,5,5]], which a tuple for the list index. So I changed it to new_favorite_foods= [favorite_foods[0:5:5]]. 
#9
if "potato" in new_favorite_foods:
    print("A potato!")
else:
    print("No potato!")

#Slicing and Striding
numbers = list(range(0,21))

#1
def get_first_15(numbers):
    return(numbers[0:15])

#2
def get_every_5th(lst):
    return(lst[::5])

#3
def reverse_and_stride(lst):
    reversed_list = lst[::-1]
    return(reversed_list[::3])

lst1 = get_first_15(numbers)
lst2 = get_every_5th(lst1)
lst3 = reverse_and_stride(lst2)

print(lst1)
print(lst2)
print(lst3)

#Nested lists
numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
] 
#1
print(numbers[2])
#2
print(numbers[1][1])
#3
numbers.append([10,11,12])
#4
def sum_nested(numbers):
    total = 0
    for row in numbers:
        for number in row:
            total += number
    return total

#5x5 list
def new_list():
    list= []
    number = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(number)
            number += 1
        list.append(row)
    return list

list_to_25 = new_list()
#1
def replace():
    modified_list = []
    for row in list_to_25:
        new_row = []
        for number in row:
            if number % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(number)
        modified_list.append(new_row)
    return modified_list

new_list_to_25 = replace()
print(new_list_to_25)
#2
def sum():
    total = 0
    for row in new_list_to_25:
        for number in row:
            if number != "?":
                total += number
    return total

sum_of_nonquestionmarks = sum()

print(sum_of_nonquestionmarks)

# ---- Dictionaries ----#
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia":25,
    "Mira": 48
}

#1
print(ages["Katie"]) #ERROR I encountered this error: AttributeError: 'dict' object has no attribute 'value'. I originally wrote: print(ages.value[0]), but all I had to do was type print(ages["Katie"]). I just forgot how to do this. 

#2
ages["Mira"]= 100

#3
ages["Milana"]= 52

#4
del ages["Mariam"]

#5
for key,value in ages.items():
    print(f"{key}" ":" f"{value}")

#---- Running Favorite Function ----#
print(sum_nested( [
    [4,9,8],
    [7,6,3],
    [0,2,4]]
))