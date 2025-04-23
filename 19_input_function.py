# Input function is used to take user input, it always returns the values as a string.
 
user_input = input("Enter your input: ")    # Does not require a print() function to prompt for user input, However a print function will be required to print out the user input
print(type(user_input))
#print(user_input)


# Explicit conversion can be used to convert str() data type to any desired data type
# However while converting explicitly, any other data type input may lead to an error (user input validation is required)

usr_inp = int(input("Enter a number: "))
print(type(usr_inp))
#print(usr_inp)

 

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
result = row1,row2,row3
print(result)

# Without validating user input

position_index = int(input("Choose an index position between (0-2): "))

# With validating user input

def usr_input():
    
    #variables
    #Initial
    position_index = ''
    acceptable_range = range(0,2)
    within_range = False

    # Two conditions to check
    # Digit or withing_range==False
    while position_index.isdigit() == False or within_range == False:
        position_index = input("Choose an index position between (0-2): ")

        # Digit Check
        if position_index.isdigit() == False:
            print("Sorry! Thats not a digit, please enter an integer")

        # Range check
        if position_index.isdigit() == True:
            if int(position_index) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of acceptable range (0-2)")
                within_range = False

    return int(position_index)

usr_input()