#A variable is a reserved memory location assigned (represented as a reference or pointer, e.g. 'used_books') to a value, equation etc.

number_of_dogs_owned = 2

# A variable cannot start with a number
# There should not be space, use underscore instead
# Cannot use special characters
# Should not be a reserved word (e.g. if, else, str, list, or)

a = 5.0             # Variable assignment
print(a)            # Output: 5.0 

a = a + a           # Variable reassignment / Mutated variable
print(a)            # Output: 10.0 

a = a + a           # again variable reassignment / Mutated variable
print(a)            # Output: 20.0 

#use "type()" function to fetch the data type of the variable

print(type(a))

#Functional example

my_income = 32000
tax_rate = 0.05
tax_amount = my_income * tax_rate
print(tax_amount)