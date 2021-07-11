#Examples from learnpython.org

x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# The in operator
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

#If statement
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

#not operator

print(not False) # Prints out True
print((not False) == (False)) # Prints out False

#Example

number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if len(second_array) == 2:
    print("2")

if len(first_array) + len(second_array) == 5:
    print("3")
