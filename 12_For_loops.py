# Many objects in python are "iterable", meaning we can iterate over every element in the object or every character in a string.

mylist = [0,1,2,3,4,5,6,7,8,9,10]


for jelly in mylist:
    print(jelly)

for txtxtxt in mylist:
    print("Hello!")     #it will print "Hello!" for each element in the list

for num in mylist:      #Initialize for loop
    if num % 2 == 0:    #Create a control flow/condition for checking even or odd numbers
        print(f"Even number : {num}")
    else:
        print(f"Odd number  : {num}")


list_sum = 0                    #initiated list sum with 0

for num in mylist:
    list_sum = list_sum + num   #for each number in the list, add it to the initial sum and store it on the same variable
print(list_sum)

for num in mylist:      #Initialize for loop
    if num <= 5:        #Create a control flow/condition for all numbers below 5 including itself
        print(num)

#Tuple unpacking

mylist = [(1,2),(3,4),(5,6),(7,8)]
for ls in mylist:
    print(ls)
for (a,b) in mylist:
    print(a)
    print(b)


mylist = [(1,2,3),(3,4,5),(5,6,7),(7,8,9)]

for (a,b,c) in mylist:
    print(b)            # print only middle element
    print(c,b,a)        # print element in reverse

d = {"k1":1,"k2":2,"k3":3}

for item in d: # It will return only values from the dictionaries
    print(item)

for item in d.items():  # To get key and value pairs
    print(item)

for key,value in d.items(): # It will return either key or value depending upon the input
    print(key)

