# *args: Used to pass a variable number of non-keyword arguments to a function. These arguments are collected into a tuple inside the function.
# **kwargs: Used to pass a variable number of keyword arguments to a function. These arguments are collected into a dictionary inside the function.


def myfunc(a,b,c=0,d=0,e=0):
  # Returns 10% of the sum of a and b
  return sum((a,b,c,d,e)) * 0.1

print(myfunc(20,40,5,5,5)) # if anymore arguments added here in function call, it will lead to an error since its not present in the function

# hence alternate - *args
def mynewfunc(*args):
  return sum(args) * 0.1
print(mynewfunc(1,2,3,4,5,6,7,8,9,100)) # here we can add n number of non keyword arguments

# **kwargs - keyword arguments
def myfunc2(**kwargs):
  if "fruit" in kwargs:
    print("My fruit of choice is {}".format(kwargs["fruit"]))
  else:
    print("I did not find any fruit here.")
myfunc2(fruit="apple",veggie='lettuce')


# next example
def my_function(*args, **kwargs):
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

# Example usage
my_function(1, 2, 3, name="Alice", age=30)