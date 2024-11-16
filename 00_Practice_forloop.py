# sum_of_range = 0
# start_of_rng = int(input("Enter Start: "))
# end_of_rng = int(input("Enter End: "))
# for num in range(start_of_rng,end_of_rng+1):
#     sum_of_range += num
# print(sum_of_range)



# start_of_rng = int(input("Enter Start: "))
# end_of_rng = int(input("Enter End: "))
# print("\fFollowing are the even numbers: ")
# for num in range(start_of_rng,end_of_rng+1):
#     if num % 2 == 0:
#         print(num)



# start_of_rng = int(input("Enter Start: "))
# end_of_rng = int(input("Enter End: "))
# num_list = [num for num in range(start_of_rng,end_of_rng+1)]
# print(num_list)



# sum_of_range = 0
# start_of_rng = int(input("Enter Start: "))
# end_of_rng = int(input("Enter End: "))
# num_list = [num for num in range(start_of_rng,end_of_rng+1)]
# for num in num_list:
#     sum_of_range += num
# print(f"average = {sum_of_range/len(num_list)}")
# print(f"Min = {min(num_list)}")
# print(f"Max = {max(num_list)}")



# tst_string = "This is test string"
# reverse_string = ""
# for i in tst_string[::-1]:
#     reverse_string += i
# print(reverse_string)



# for i in range(3):
#     for j in range(5):
#         print("*", end="")
#     print()


# num_of_rows = int(input("Enter Number of Rows: "))
# num_of_columns = int(input("Enter Number of Columns: "))
# for i in range(num_of_rows):
#     for j in range(num_of_rows - i - 1):
#         print(" ",end="")
#     for j in range(i*2+1):
#         print("*",end="")
#     if j == num_of_columns:
#         print()
#         break
#     print()



# num_of_rows = int(input("Enter Number of Rows: "))
# num_of_columns = int(input("Enter Number of Columns: "))
# for i in range(num_of_rows):
#     for j in range(num_of_rows - i - 1):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")
#     if j == num_of_columns:
#         print()
#         break
#     print()