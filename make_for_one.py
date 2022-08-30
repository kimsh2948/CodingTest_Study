x = int(input())

list = [0, 0, 1, 1]

for i in range(4, x+1):
    list.append(list[i-1] + 1)

    if i%2 == 0:
        list[i] = min(list[i//2]+1, list[i])
    if i%3 == 0:
        list[i] = min(list[i//3]+1, list[i])

print(list[x])
