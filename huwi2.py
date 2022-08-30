import sys

count = int(input())

math_arr = input()
num_arr = [0] * count

for i in range(count):
    num_arr[i] = int(input())

stack = []

for i in math_arr:
    if 'A' <= i <= 'Z':
        stack.append(num_arr[ord(i) - ord('A')])
    else:
        stk2 = stack.pop()
        stk1 = stack.pop()

        if i == '+':
            stack.append(stk1 + stk2)
        elif i == '-':
            stack.append(stk1 - stk2)
        elif i == '*':
            stack.append(stk1 * stk2)
        elif i == '/':
            stack.append(stk1 / stk2)

print('%.2f' % stack[0])


