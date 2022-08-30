n = int(input())

list = [0, 1, 3]

for i in range(3, n+1):
    list.append(list[i-1] + list[i-2] * 2)

print(list[n] % 10007)