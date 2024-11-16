# range(start, end, step size) - This function gives all the numbers within specified range

for num in range(0,25+1,2):
    print(num)

# list()
new_list = list((range(0,14+1)))
print(new_list)


# .format()
    #.format() function can be used to format a string, make it more dynamic.
i = 0

for letter in "asdfghjkl":
    print("The letter at index {} is {}".format(i,letter))
    i += 1

# enumerate()
    # Enumerate function returns index number and the iterable character/object in form of a tuple for EACH iteration.
    # Hence we can use tuple unpacking here
word = "asdfghjkl"
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print("\n")


# zip()
    # The zip function zips two or more lists/iterables together into tuples for EACH iterable.
    # If the lists/iterables are uneven, it will only consider the least number of iterable present for all the list.
mylist1 = [100,200,300,400,500,600]
mylist2 = ["a","b","c","d"]
mylist3 = [1,2,3]

for x,y,z in zip(mylist1,mylist2,mylist3): #zip function will create tuples & x,y,z can help with tuples unpacking
    print(x)
    print(y)
    print(z)

print(list(zip(mylist1,mylist2,mylist3)))


# in
    # The in operator checks if something is present in a list or iterable

list_in = [1,2,3,4,5,6,7]
print(3 in list_in)

blist=[]
for character in "happy birthday!!!":
    if character == "a":
        blist.append(character)
        print(blist)

d = {'mynum':33224}
if 33224 in d.values():
    print(d.keys())


# min() & max()
my_new_list = [10,20,30,40,55,64,32,5,12,96,354]
print(min(my_new_list))
print(max(my_new_list))

#random (Library)
import random
listed = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(listed) # shuffle is an inplace function - An in-place function is a function that modifies the data it receives directly, without creating a new copy. 
print(listed)

rand_num = random.randint(0,100)
print(rand_num)

#input()
    #The input function allows the users to give an input - by default its a string, casting can be used for integer etc.

usr_input = int(input("Enter an integer of your choice: "))
print(usr_input)