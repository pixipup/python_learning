# Lists are ordered sequence of variety of objects.
# They use [] and commas to separate objects in the list.
# e.g. [1,2,3,4,5]
# Lists supports indexing and slicing.
# Lists can be nested.

my_list = [1,2,3,4,5,323]
print(my_list)

print(my_list[2:]) #List Slicing
print(my_list[3]) #Indexing

another_list = [6,7,8,9]

new_list = my_list + another_list # concatenate lists
print(new_list) 

# Lists are mutable

new_list[0] = '75'

print(new_list)

new_list.append(my_list) # Add an element at the end of the list, in this case add a list within a list, known as nested list
print(new_list)

popped_element = new_list.pop() #delete or pop the last element of the list [Additional note: (.pop when assigned to a variable; returns popped object)]
print(popped_element)

new_list.pop(3) #delete or pop the indexed element from the list
print(new_list)


new_list = ['y','f','b','x','a']
new_list.sort(reverse=True)
print(new_list)


new_list = ['y','f','b','x','a']
new_list.reverse()
print(new_list)