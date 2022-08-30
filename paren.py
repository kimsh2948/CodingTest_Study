count = int(input())

for i in range(count):
    stack = []
    check = 0
    paren = input()
    for j in paren:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if len(stack) == 0:
                print("NO")
                check=1
                break
            else:
                stack.pop()
    if check == 0: 
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")

