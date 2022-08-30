n = int(input())

sq_list = []

sq_list.append(0)
sq_list.append(1)
sq_list.append(3)

for i in range(3, n+1):
    sq_list.append(sq_list[i-1] + 2*sq_list[i-2])

print(sq_list[n] % 10007)

