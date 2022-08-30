middle = list(input())
stack = []

for i in range(len(middle)):
    if 'A' <= middle[i] <= 'Z':
        stack.append(middle.pop(i))

#for i in range(len(middle)):
    


