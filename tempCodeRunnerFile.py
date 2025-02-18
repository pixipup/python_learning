def main():
    b = []
    n = int(input())
    
    for _ in range(n):
        operation = input().split()
        
        if operation[0] == 'insert':
            b.insert(int(operation[1]), int(operation[2]))
        elif operation[0] == 'print':
            print(b)
        elif operation[0] == 'remove':
            b.remove(int(operation[1]))
        elif operation[0] == 'append':
            b.append(int(operation[1]))
        elif operation[0] == 'sort':
            b.sort()
        elif operation[0] == 'pop':
            b.pop()
        elif operation[0] == 'reverse':
            b.reverse()
        else:
            print("Invalid operation")

    main()