# list = [2, 44, 72, 37, 5, 99, 20]

# # Printing minimum and maximum number from the list
# print(f"Maximum number in the {list} is {max(list)}")
# print(f"Minimum number in the {list} is {min(list)}")



# # Sorting the list using sort function

# sorted_list = list.copy()
# sorted_list.sort()
# print(f"Ascending order: {sorted_list}")

# sorted_list.sort(reverse=True)
# print(f"Descending order: {sorted_list}")


# # Sorting the list using for loop

# new_sorted_list = list.copy()

# for i in range(0, len(new_sorted_list)-1):
#     for j in range(i+1,len(new_sorted_list)):
#         if new_sorted_list[i] > new_sorted_list[j]:
#             new_sorted_list[i],new_sorted_list[j] = new_sorted_list[j],new_sorted_list[i]
# print(new_sorted_list)
# new_sorted_list.reverse()
# print(new_sorted_list)


# # Simple math operations taking dynamic inputs

# first_number = int(input("\nEnter 1st number: "))
# operator = input("\n+ = Addition \n- = Subtraction \n/ = Division \n* = Multiplication \n\nEnter one of the above operator for desired operation: ")
# second_number = int(input("\nEnter 2nd number: "))

# if operator == "-":
#     solution = first_number - second_number
# elif operator == "+":
#     solution = first_number + second_number
# elif operator == "*":
#     solution = first_number * second_number
# elif operator == "/":
#     solution = first_number / second_number
# else:
#     print("Invalid input.")
# print(solution)


# # Sort list according to length of string object in a list

# name_list = ["Sai", "Harsh", "Prem", "Venkat", "Apple", "Orange"]

# for i in range(0, len(name_list)-1):
#     for j in range(i+1,len(name_list)):
#         if len(name_list[i]) > len(name_list[j]):
#             name_list[i],name_list[j] = name_list[j],name_list[i]
# print(name_list)
# name_list.reverse()
# print(name_list)


# # Print even numbers till 20

# x = 0
# while x <= 20:
#     if x % 2 == 0:
#         print(x)
#     x += 1



# Add elements (34, 72, 83, 45, 27, 2, 9) in a list and print the list

# empty_list = []
# while True:
#     user_input = input("Enter an integer (type 'end' to stop): ")
#     try:
#         number = int(user_input)  # Attempt conversion to integer
#         empty_list.append(number)  # Append only if successful
#         continue  # continue loop after valid integer input
#     except ValueError:
#         if user_input.lower() == "end":  # Handle 'end' case gracefully
#             break
#         else:
#             print("Invalid input. Please enter an integer or 'end' to stop.")
# print(empty_list)

# print(f"Maximum number in the list is: {max(empty_list)}")
# print(f"Minimum number in the list is: {min(empty_list)}")

# new_list = empty_list.copy()
# odd_list = []
# even_list = []
# for i in range(0,len(new_list)+1):
#     if i % 2 == 0:
#         odd_list.append(i)
#     elif i % 2 == 1:
#         even_list.append(i)
# print(odd_list)
# print(even_list)




# def display_menu():
#   """Prints the menu options."""
#   print("\nMenu:")
#   print("1. View Message")
#   print("2. Play a Game")
#   print("3. Exit")

# def main():
#   """Runs the main menu loop."""
#   choice = "0"
#   while choice != "3":
#     display_menu()
#     choice = input("Enter your choice (1-3): ")

#     if choice == "1":
#       print("This is a secret message!")
#     elif choice == "2":
#       print("Let's play a simple guessing game!")
#       import random
#       secret_number = random.randint(1,100)          # Generate a random number for user to guess
#       max_guess = 10          # Enter the maximum number of guess
#       num_of_guess = 0        # Initialize current guess number

#       print("I'm thinking of a number between 1 and 100. You have", max_guess, "guesses to find it.")

#       while num_of_guess < max_guess:
#         # Get the user's guess
#         try:
#             guess = int(input("Take a guess: "))
#         except ValueError:
#             print("Invalid input. Please enter a whole number between 1 and 100.")
#             continue

#         # Check if the guess is within the valid range
#         if guess < 1 or guess > 100:
#             print("Your guess is out of range. Please enter a number between 1 and 100.")
#             continue
        
#         num_of_guess += 1

#         # Provide hints based on the guess
#         if guess == secret_number:
#             print("Congratulations! You guessed the number in", num_of_guess, "guesses.")
#             break
#         elif guess > secret_number:
#             print("Your guess is too high. Try again.")
#         else:
#             print("Your guess is too low. Try again.")

#         #   Handle the case where the user runs out of guesses
#         if num_of_guess == max_guess:
#             print("Sorry, you ran out of guesses. The number was", secret_number)
    
#     elif choice == "3":
#       print("Exiting...")
#     else:
#       print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#   main()



(a,b,c,d) = (1,2,3,4)
print(a)
print(b)
print(c)
print(d)
