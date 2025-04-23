# x = 0
# while x <= 20:
#     if x % 2 == 0:
#         print(x)
#     x += 1



# usr_inp = int(input("Enter number upto which you want to print: "))
# x = 0
# sum = 0
# while x < usr_inp + 1:
#     # print(x)
#     sum = sum + x
#     x += 1
# print(sum)




# x = int(input("Enter a number: "))
# while x >= 1:
#     print(x)
#     x-=1






# row_size = int(input("Enter the row length of the square: "))
# column_size = int(input("Enter the column length of the square: "))
# c_row = 0
# while c_row < row_size:
#     c_column = 0
#     while c_column < column_size:
#         print("*",end = "")
#         c_column += 1
#     print()
#     c_row += 1







# import random           
# secret_number = random.randint(1,100)          # Generate a random number for user to guess
# max_guess = 10          # Enter the maximum number of guess
# num_of_guess = 0        # Initialize current guess number

# print("I'm thinking of a number between 1 and 100. You have", max_guess, "guesses to find it.")

# while num_of_guess < max_guess:
#     # Get the user's guess
#     try:
#       guess = int(input("Take a guess: "))
#     except ValueError:
#       print("Invalid input. Please enter a whole number between 1 and 100.")
#       continue

#     # Check if the guess is within the valid range
#     if guess < 1 or guess > 100:
#       print("Your guess is out of range. Please enter a number between 1 and 100.")
#       continue
    
#     num_of_guess += 1

#     # Provide hints based on the guess
#     if guess == secret_number:
#       print("Congratulations! You guessed the number in", num_of_guess, "guesses.")
#       break
#     elif guess > secret_number:
#       print("Your guess is too high. Try again.")
#     else:
#       print("Your guess is too low. Try again.")

#     #   Handle the case where the user runs out of guesses
#     if num_of_guess == max_guess:
#         print("Sorry, you ran out of guesses. The number was", secret_number)






# def factorial(n):
#   """Calculates the factorial of a non-negative integer."""
#   if n < 0:
#     raise ValueError("Factorial is not defined for negative numbers.")
#   result = 1
#   for i in range(1, n + 1):
#     result *= i
#   return result

# while True:
#   try:
#     num = int(input("Enter a non-negative integer: "))
#     if num >= 0:
#       break
#     print("Please enter a non-negative number.")
#   except ValueError:
#     print("Invalid input. Please enter an integer.")

# factorial_result = factorial(num)
# print("The factorial of", num, "is:", factorial_result)