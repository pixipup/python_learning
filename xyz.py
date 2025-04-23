n = int(input("Number of students:"))

student_marks = {}

for i in range(n):

    name, *line = input("Enter name< >marks1< >marks2< >marks3...followed by enter: ").split()

    scores = list(map(float, line))

    student_marks[name] = scores

query_name = input()

l1 = list(student_marks[query_name]) 

addition = sum(l1)

result = addition/len(l1)

print('%.2f'% result)