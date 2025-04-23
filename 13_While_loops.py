# While loops will continue to execute a block of code while some condition is True.

x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print("x is not less than 5")


# break, continue, pass

# break: Breaks out of the current closest enclosing loop
# continue: Goes to the top of the closest closest enclosing loop
# pass: Does nothing at all (like a place holder)

x = 0               #initiate a variable
while x < 5:
    x += 1          #increment
    if x == 3:      #condition
        # x += 1      #increment and continue
        continue
    print(f'The current value of x is {x}')
    

x = 0               #initiate a variable
while x < 5:
    x += 1          #increment
    if x == 4:      #condition
        break       #Break
    print(f'The current value of x is {x}')