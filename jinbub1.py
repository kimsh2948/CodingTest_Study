n, b = input().split()
n = "".join(reversed(n))
b = int(b)
alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0
sum = 0

for i in range(len(n)-1, -1, -1):
    sum = alpha.index(n[i]) * (b ** i)
    result += sum

print(result) 
