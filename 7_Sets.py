# Sets are unordered collection of unique elements.
# syntax = set()

my_set = set()

print(my_set)

my_set.add(1)
my_set.add(2)
my_set.add(2) # adding same element 2nd time wont add it to the set twice.
print(my_set)

my_list = ['Sam','Sam','Gary','Sam','Jake','Gary']
print(set(my_list))

new_list = list(set(my_list)) # converting sets to list by calling list function explicitly
print(new_list)

# set wont return the elements in sequence they are entered or present in the set, it is randomized