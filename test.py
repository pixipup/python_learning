#
st = 'Print only the words that starts with s in this sentence'
for letter in st.split():
    if letter[0] == "s":
        print(letter)

#
ls = [x for x in range(0,10+1) if x%2==0]
print(ls)


#
ls = [x for x in range(0,50+1) if x%3==0]
print(ls)

#
st = 'Print only the words that has an even number of letters in this sentence'
for letter in st.split():
    if len(letter)%2 == 0:
        print(letter)

#
for num in range(0,100+1):
    if num%3 == 0 and num%5 == 0:
        print(num, "= FizzBuzz")
    elif num%3 == 0:
        print(num, "= Fizz")
    elif num%5 == 0:
        print(num, "= Buzz")

#
st = 'Create a list of the first letters of every word in this string'
new_list = [letter[0] for letter in st.split()]
print(new_list)