n, b = map(int, input().split())

alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

sum = 0
result = []

while n > 0:
    sum = n % b
    n = n // b
    result.append(alpha[sum])

result = "".join(reversed(result))
print(result)