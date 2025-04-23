# List comprehensions are a concise and powerful way to create new lists in Python. They provide a single-line syntax to iterate over an existing iterable (like a list, string, or tuple) and generate a new list based on some condition or transformation.

#traditional method
mystring = "Hey, World!"
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

# List comprehensions
mystring = "Hey, World!"
mylist = [letter for letter in mystring]
print(mylist)


# Operation in LC

mylist = [num**2 for num in range(1,15)] # 1st element is where you can perform operations, like in this example we are finding num square.
print(mylist)


# IF statements in LC

mylist = [num for num in range(1,15) if num%2==0]
print(mylist)

# Example

celcius = [0,10.7,17.2,55.3]
fahrenheit = [((9/5)*temp+32) for temp in celcius]
print(fahrenheit)

# Example - with LC

mylist = [x*y for x in [1,10,100] for y in [1,2,3]]
print(mylist)

# Without LC
mystring = [1, 10, 100]
anothermystring = [1, 2, 3]
mylist = []

for x in mystring:
    for y in anothermystring:
        mylist.append(x * y)

print(mylist)