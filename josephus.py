#다시 풀어볼것
n, k = map(int, input().split())

queue = []
num_arr = []
index = k-1

for i in range(1, n+1):
    queue[i] = i

for j in range(n):
    num_arr.append(queue.pop(index))
    if index >= len(queue) - 1:
        index = index % len(queue)

print("<", ",".join(num_arr)[:], ">", sep='')



