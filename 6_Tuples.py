# Tuples are similar to lists, however they are immutable.
# lists - [] and tuples - ()

my_tuple = (1,2,3)
my_list = [1,2,3]

print(type(my_list))
print(type(my_tuple))

# slicing and indexing is possible to lists

print(my_tuple.count(2))    # count of integer "2" in tuple.
print(my_tuple.index(3))    # index position of integer "3" in tuple.

my_list[0] = 45
my_list.append(31)
my_list.pop()
print(my_list)


my_tuple[0] = 45
print(my_tuple)
#The above statement will result in error as tuples are not mutable