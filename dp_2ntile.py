n = int(input())

sq_list = []

sq_list.append(1)
sq_list.append(2)

for i in range(2, n):
    sq_list.append(sq_list[i -1] + sq_list[i-2])
    

print(sq_list[n-1] % 10007)