list = [2,44,72,37,5,99,20]
highest_number = max(list)
lowest_number = min(list)
print(f"Highest number = {highest_number} and lowest number = {lowest_number}")

# Sorting using sort function
list.sort()
print(f"Ascending list: {list}")
list.sort(reverse=True)
print(f"Decending list: {list}")

# Sorting using for loop
list = [2, 44, 72, 37, 5, 99, 20]
sorted_list = list.copy()
for i in range(0, len(sorted_list) - 1):
    for j in range(i + 1, len(sorted_list)):
        if sorted_list[j] < sorted_list[i]:
            sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
print(sorted_list)

