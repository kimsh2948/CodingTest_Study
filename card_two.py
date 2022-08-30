from collections import deque
import sys

count = int(sys.stdin.readline())
deq = deque()

for i in range(1, count+1):
    deq.append(i)

while len(deq) != 1:
    deq.popleft()
    tmp = deq[0]
    deq.popleft()
    deq.append(tmp)

print(deq[0])
