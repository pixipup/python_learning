# Strings are ordered sequence of characters
# Syntax: Single or double quotes "" ''

# "Hello" , 'Hello'

# String indexing : use [] after string

# Character     : H  e  l  l  o
# Index         : 0  1  2  3  4
# Reverse Index : 0 -4 -3 -2 -1

# Indexing is used to grab a certain character

# String slicing : use [start:stop:step] after string
# Slicing is similar to indexing but it is used to grab a sequence of characters instead of only one.
# e.g. "Welcome"[-4:] -> it will give last 4 characters of the string
# Use len() function to identify length of the string.

MyString = "Welcome"
print(MyString[3])
print(MyString[::-1]) # Reverse string
print(MyString[-4:])
lengthofmystring = print(len(MyString))

# If your string contains a single quote or double quote in itself, then use the opposite quote outside to make it a string.

# Escape characters: These are the characters which are used within a string to format the string appears.
# E.g. \n -> for new line
#      \t -> for Tab
# "Hey, it's me. \n Call me back."

print("Hey, it's me. \nCall me back.")
print("Hey, it's me. \tCall me back.")

# Strings are immutable
# e.g. name = Sam
#      name[0] = P -> will result in error and will not change the string from Sam to Pam.

# Use "+" to concatenate strings

print("2" + "3")

# To modify or get advanced options for strings, you can use "." after the variable to get a list of options.
x = "hello world"
print(x.upper())

# .upper()
# .lower()
# .capitalize()
# .split() and many more


# To format a strings, you can use ".format(V1, V2, V3)" after the string where V1, V2, V3 represent variables. Use "{}" in the strings as a place holder for those variables.
SubjectName = "Sam"
myage = 24
x = "hello {}, I am turning {} year old today.".format(SubjectName, myage)
print(x)
# You can use index numbers in the curly bracket to call objects from index position.

# You can use F strings to create a formatted string instead of using .format methods.

distance = '35km'
print(f"My house is {distance} away.")

# 
name="Paul"
age="24"
x = f"hello {name}, I am turning {age} year old today."
print(x)

