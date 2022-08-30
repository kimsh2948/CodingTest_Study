n = int(input())

stack = []
result = []
count = 1
check = True

for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        check = False

if check == True:
    for j in result:
        print(j)
else:
    print("NO")
    
    
