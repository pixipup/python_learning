# In Python, functions are reusable blocks of code that perform specific tasks. They offer several advantages
# Modularization: Functions break down complex programs into smaller, manageable pieces, making code easier to read, understand, and maintain.
# Reusability: You can define a function once and use it multiple times throughout your program, or even in other programs, reducing code duplication.
# Encapsulation: Functions can group related code and data together, hiding internal implementation details and promoting better organization.

# use "def" followed by the function name to create a function

# Function without an argument
def numbers():
    for x in range(1,10+1):
        print(x)
numbers()


# Same Function with an argument/variable
def numbers(a,b,c):
    for x in range(a,b,c):
        print(x)
numbers(0,10+1,2)

# Function with an argument/variable
def greetings(name="Default"):          # a default argument can be assigned in case the function called without a variable.
    print(f"Hello, How are you {name}?")
greetings()
greetings("Alex")

# Return keyword

# the return keyword, instead of just printing out something, will allow user to assign that something (integer, string etc) to a variable.
# the return keyword also ends the function call.

def add_num(num1,num2):
    return num1+num2    # It will not print untill called upon.

x = add_num(2,4) # we can assign that function now to a variable.
print(x)


def even_check(number):
    if number % 2 == 0:
        return True
    elif number % 2 != 0:
        return False


number = int(input("Enter any integer: "))
if even_check(number) is True:
    print(f"{number} is even")
elif even_check(number) is False:
    print(f"{number} is odd")


def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass        # the pass statement will do nothing if the condition is false. If we use "return False" also within the for loop, it will only check the first element in the list, as the return function will end the function call after 1st element.
    return False

my_even_list = check_even_list([1,3,9])
print(my_even_list)

my_even_list = check_even_list([2,4,9])
print(my_even_list)


def return_even_list(num_list):
    even_number = []
    for num in num_list:
        if num % 2 == 0:
            even_number.append(num)
        else:
            pass        # the pass statement will do nothing if the condition is false. If we use "return False" also within the for loop, it will only check the first element in the list, as the return function will end the function call after 1st element.
    return even_number

# print(return_even_list([1,2,3,4,5,6,7,8,9,0]))


# Tuples unpacking using functions

age_group = [("sam", 14),("gary", 20),("lisa", 16),("joy", 23)]

def age_sort(age_group):

    current_age = 0
    given_name = ""

    for name, age in age_group:
        if age > current_age:
            current_age = age
            given_name = name
        else:
            pass

    return current_age, given_name


result = age_sort(age_group)
print(result)




