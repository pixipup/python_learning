
# Initiate function for even odd, min max condition
def lesser_of_two_evens(x,y):
    if x%2==0 and y%2==0:
        return min(x,y) # minimum if both are even
    else:
        return max(x,y) # maximum if one or both are not even
test = lesser_of_two_evens(2,5)
print(test)


# Initiate function for animal crackers - two word sring, if inital letters are same return true else false
def animal_crackers(text):
    wordlist = text.lower().split()
    return wordlist[0][0] == wordlist[1][0]

xyz = animal_crackers('Crazzy Krock')
print(xyz)


# Initiate function - if sum of two int is 20 or one of the int is 20 return true else false
def makes_twenty(x,y):
    return x == 20 or y == 20 or x+y == 20
        
test1 = makes_twenty(14,6)
print(test1)



# Level 1 problems

# Write a function to capitalize 1st and 4th letters of a name

def namecap(namestring):
    if len(namestring) < 4:
        return namestring.capitalize()
    return namestring[0].upper() + namestring[1:3] + namestring[3].upper() + namestring[4:]
print(namecap("usama"))


# Write a function to reverse the words in a sentence "How are you" -> "you are How"

def revsen(my_sentence):
    word_list = my_sentence.split()
    reverse_word_list = word_list[::-1]
    reverse_string = " ".join(reverse_word_list)
    return reverse_string

print(revsen("Hope your flight was comfortable"))


# Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10) # abs() - absolute function

print(almost_there(96))

# Level 2 problems

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(number_list):
    for i in range(0,len(number_list)-1):
        if number_list[i] == 3 and number_list[i+1] == 3:
            return True
    return False
print(has_33([1,2,3,3,0,5]))


# Paper Doll : Given a string where for every character in the original there are three characters
# paper_doll("Hello") -> HHHeeellllllooo

def paper_doll(my_string):
    new_string = ""
    for letter in my_string:
        new_string = new_string + letter*3
    return new_string
print(paper_doll("Hey"))

# BLACKJACK game

def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c])-10 > 21:
        return "bust"
    else:
        return sum([a,b,c]) - 10
        
print(blackjack(9,9,9))


# Summer of "69": Return the sum of the numbers in the array, except ignore sections of the numbers starting with 6 and extending to the next 9 (Every 6 will be followed by atleast one 9). Return 0 for no numbers.
# summer_69([2,1,6,9,11]) --> 14

def summer_69(num_list):
    total = 0
    add = True

    for num in num_list:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_69([2,4,5,6,8,7,9,3]))


# Challenging problems

# Create a spy game, In a list of integers if 007 is present in sequence eg [1,3,2,4,0,5,7,2,0,7,5] then return true.

def spy_game(spy_list):
    code = [0,0,7,"e"]
    for i in spy_list:
        if i == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game([1,3,2,2,4,0,8,0,7,5]))

 # Count Primes: Write a function that returns the number of prime numbers that exist up to and including a given number.
 # By convention 0 and 1 are not prime

def count_primes(num):
   
    # Check for 0 or 1 input
    if num < 2:
        return 0
    
    #####################
    # 2 or greater
    #####################

    # List to store out prime numbers
    primes = [2]
    # Counter going up to the input num
    x = 3

    # x is going through every number up to input num
    while x <= num:
        # Check if x is prime
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(100))


# Write a function to calculate volume of a sphere (4/3 X PIE X radius cube)

def sphere_vol(rad):
    return (4/3)*(3.14)*(rad**3)

print(sphere_vol(2))

# Write a function that checks wether a number is in a given range (Inclusive of high and low)

def ran_check(num,low,high):
    if num in range(low,high+1):
        print(f"{num} is in the range {low} and {high}")
    else:
        print(f"{num} is not in the range {low} and {high}")

ran_check(3,1,6)


def ran_bool(num,low,high):
    if num in range(low,high+1):
        return True
    else:
        return False

print(ran_bool(3,1,6))



# Write a function that accepts a string and calculates the number of upper case letters and lower case letters.

def low_up(my_string):
    lowercase = 0
    uppercase = 0
    for letter in my_string:
        if letter.isupper():
            uppercase += 1
        elif letter.islower():
            lowercase += 1
        else:
            pass
    print(f"Original string: {my_string}")
    print(f"lowercase count: {lowercase}")
    print(f"uppercase count: {uppercase}")
low_up("Hey, How are you? Didnt saw you In a long Time")

# OR we can use dictionary

def low_up(my_string):
    d = {'upper':0,'lower':0}
    for letter in my_string:
        if letter.isupper():
            d['upper'] += 1
        elif letter.islower():
            d['lower'] += 1
        else:
            pass
    print(f"Original string: {my_string}")
    print(f"lowercase count: {d['lower']}")
    print(f"uppercase count: {d['upper']}")
low_up("Hey, How are you? Didnt saw you In a long Time")


# Write a python function that takes a list and returns a new list with unique elements of the first list

def unique_list(lst):
    new_list = []
    for x in lst:
        if x not in new_list:
            new_list.append(x)
        else:
            pass
    return new_list

print(unique_list([1,1,2,3,4,4,2,3,5,6,3,4]))

# OR we can use set()

def unique_list(lst):
    return list(set(lst))

print(unique_list([1,1,2,3,4,4,2,3,5,6,3,4]))

# Write a python function to multiply all the numbers in a list

def mul_num(mlst):
    total_product = 1
    for x in mlst:
        total_product = total_product * x
    return total_product

print(mul_num([1,2,3,-4]))

# Wite a function that checks whether a word or phrase is palindrome or not.

def palindrome(p):
    p = p.replace(' ','')  # Remove all spaces
    reversed_phrase = p[::-1]
    if p == ''.join(reversed_phrase):
        print(f"The string {p} is a palindrome")
    else:
        print(f"The string {p} is not a palindrome")

palindrome("wow racecar wow")

# OR

def palindrome(p):
    p = p.replace(' ','')  # Remove all spaces
    if p == p[::-1]:
        print(f"The string {p} is a palindrome")
    else:
        print(f"The string {p} is not a palindrome")

palindrome("not a palindrome")


# Write a function to check wether a string is pangram or not (pangram = each letter of alphabets atleast once)
# e.g The quick brown fox jumps over the lazy dog

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    
    # Crete a set of entire alphabet
    alphaset = set(alphabet)
    # Remove spaces from input string
    str1 = str1.replace(' ','')
    # Convert into all lowercase
    str1 = str1.lower()
    # Grab all unique letters from the string set()
    str1 = set(str1)
    # Alphabet set == string set input
    return str1 == alphaset

print(ispangram("The quick brown fox jumps over the lazy dog"))