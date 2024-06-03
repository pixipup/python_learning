multiplication_number = int(input("Enter multiplication number: "))
multiplication_limit = int(input("Enter multiplication limit: "))
print()
j = 1
while j <= multiplication_limit:
    product = multiplication_number * j
    print(f"{multiplication_number} X {j} = {product}")
    j = j + 1
print()