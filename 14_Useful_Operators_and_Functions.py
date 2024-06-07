# range(start, end, step size) - This function gives all the numbers within specified range

for num in range(0,25+1,2):
    print(num)

# list()
new_list = list((range(0,14+1)))
print(new_list)


# .format()
i = 0

for letter in "asdfghjkl":
    print("The letter at index {} is {}".format(i,letter))
    i += 1

# enumerate()
word = "asdfghjkl"
for index, letter in enumerate(word):       # It returns the index and number at that index in form of tuple, hence we can use tuple unpacking here
    print(index)
    print(letter)
    print("\n")


# zip()

