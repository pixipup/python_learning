
import math

print(4**2)
print(4**2)
print(50**0.5)
print(math.sqrt(50))

#strings
s = "hello"
print(s[1])
print(s[::-1])
length_of_s = len(s)
print(s[length_of_s - 1])

#Lists
my_list_1 = [0,0,0]
my_list_2 = [0]
my_list_2.append(0)
my_list_2.append(0)
my_list_3 = [0]*3
print(my_list_1)
print(my_list_2)
print(my_list_3)

list3 = [1,2,[3,4,"hello"]]
(list3[2])[2] = 'goodbye'
print(list3)

list4 = [5,3,4,6,1]
print(sorted(list4))
list4.sort()
print(list4)

#Dictionaries
d = {'simple_key':'hello'} #Grab Hello
print(d['simple_key'])

d = {'k1':{'k2':'hello'}} #Grab Hello
print(d['k1']['k2'])
# d1 = d['k1']
# print(d1['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]} #Grab Hello
print(d['k1'][0]['nest_key'][1][0])


d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]} #Grab Hello
print(d['k1'][2]['k2'][1]['tough'][2][0])