# Map function - Applies a given function to each element of an iterable (like a list, tuple, or set) and returns a new iterable containing the results.
# function: The function to apply to each element.
# iterable: The iterable whose elements will be mapped

# Syntax: map(function, iterable)

# Lets create a function for example

def square(num):
    return num**2

# Now create an iterable list

my_nums = [1,2,3,4,5]

# now lets use map function for getting square of all the numbers in my_num list

print(list(map(square,my_nums)))

# Or

for item in map(square,my_nums):
    print(item)

# Or

map_func = list(map(square,my_nums))
print(map_func)


# Filter function - Creates a new iterable containing only the elements from the original iterable that satisfy a given condition.
# function: The function to apply to each element.
# iterable: The iterable whose elements will be mapped.

# Syntax: filter(function, iterable)

# Lets create a function for example

def is_even(x):
    return x % 2 == 0

# Creating an iterable list

numbers = [1, 2, 3, 4, 5, 6]

# now lets use filter function to filter out all the even numbers from the iterable list

even_numbers = filter(is_even, numbers)
print(list(even_numbers))


# Lambda expressions, also known as anonymous functions, are a concise way to define functions without giving them a name. They are often used for simple, one-time functions.

# A regular function to square a number
def square(x):
    return x * x

# Equivalent lambda expression
square_lambda = lambda x: x * x

# Using the lambda expression
result = square_lambda(5)
print(result)

# Using lambda expression or anonymous functions (because it dosent have a name) with map or filter function
print(list(map(lambda x: x * x, [1,2,3,4,5,6])))