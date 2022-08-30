count = int(input())

list = [0, 1, 2, 4]

for i in range(4, 12):
    list.append(list[i-1] + list[i-2] + list[i-3])

for i in range(count):
    n = int(input())
    print(list[n])