num1, num2 = input().split()

num1 = list(reversed(num1))
num2 = list(reversed(num2))

num1 = int(''.join(num1))
num2 = int(''.join(num2))

result = 0

if num1 > num2:
    result = num1
else:
    result = num2

print(result)

