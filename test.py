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


