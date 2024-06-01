# Dictionaries are unordered sequence of key value pairs
# Dictionaries uses curly braces {} and colons to signify the keys and their associated values.
# e.g. {'key1':'value1','key2':'value2'}

# The difference between list and dictionaries is that list uses a location (index) to retrieve an object but in dictionaries objects can be retrieved by key name.

my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)
print(my_dict['key1'])


fruit_prices = {'apple':'55','mango':'75','green_apple':'60'}
print(fruit_prices)
print(fruit_prices['mango'])
print(fruit_prices['green_apple'])

# Dictionary values can contain lists or dictionaries as well (Nesting)

d1 = {'names':['sam','jake','gary'],'age':[21,25,23]}
print(d1)
print(d1['names'][1].upper(), d1['age'][1])

my_list = d1['names']
my_list.append('clay')
print(my_list)

d = {'k1':100,'k2':200}
d['k3'] = 300           # to add new key value pair
print(d)

d['k2'] = 150           # to modify value
print(d)

print(d.keys())
print(d.values())
print(d.items())