# Temperature Conversion:
# Write a program to convert Celsius to Fahrenheit and vice versa.

def temp_conversion():
    usr_input = str(input("Converting from - Celsius or Fahrenheit : ")).lower()
    if usr_input == "celsius":
        celsius = int(input("Enter values in celsius: "))
        output = celsius*(9/5)+32
        print(output)
    elif usr_input == "fahrenheit":
        fahrenheit = int(input("Enter values in Fahrenheit: "))
        output = (fahrenheit-32)*(5/9)
        print(output)
    else:
        print("Wrong input, Check your input. celsius or fahrenheit.")
temp_conversion()
    

# Simple Interest Calculator:
# Calculate simple interest given principal, rate, and time.

def sim_int():
    principal_amount = float(input("Enter Principal amount: "))
    time_period = int(input("Enter time period in years: "))
    int_rate = float(input("Enter interest rate in percentage: "))
    total_amount = principal_amount*(1+time_period*(int_rate/100))
    print(f"Total amount after {time_period} years would be {total_amount:.2f}")
sim_int()


# Area and Perimeter of a Circle:
# Calculate the area and perimeter of a circle given its radius.

def area_peri_circle():
    PI = 3.14159

    radius = float(input("Enter the radius of the circle: "))

    area = PI * radius**2
    perimeter = 2 * PI * radius

    print("Area of the circle:", area)
    print("Perimeter of the circle:", perimeter)
area_peri_circle()


# List Manipulation:
# Create a list of numbers. Find the largest, smallest, and average.
num_list = [3,6,7,2,4,15,12,10,19,8]
print(f"Minimum number in your list is {min(num_list)}")
print(f"Maximum number in your list is {max(num_list)}")
print(f"Average number in your list is {sum(num_list)/len(num_list)}")

# List Reversal:
# Reverse a list without using the reverse() method.

num_list = [3,6,7,2,4,15,12,10,19,8]
print(num_list[::-1])

# Unique Elements:
# Remove duplicate elements from a list.

new_list = ["Sam","Jake","Paul","John","Paul","Jake"]
no_dupe = list(set(new_list))
no_dupe.sort()
print(no_dupe)

# Phonebook:
# Create a dictionary to store names and phone numbers. Allow users to search for numbers.

new_dict = {"Sam":"321456","Alice":"444333222","Jake":"3214321"}
user_input = input("Enter name: ")
if user_input in new_dict:
    print(f"Phone number for{user_input} is {new_dict[user_input]}")
else:
    print("Wrong input try again")


# Word Count:
# Count the frequency of words in a given text.


def word_count(text):

  words = text.split()
  word_count = {}
  for word in words:
    word_count[word] = word_count.get(word, 0) + 1
  return word_count

text = "This is a sample text. This text is for testing word count."
result = word_count(text)
print(result)