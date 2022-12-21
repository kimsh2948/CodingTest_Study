from collections import deque

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

graph = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [0] *  (n+1)
count = 0
answer = []

def dfs(x, y, count):
    print(x, y)
    count += 1
    visited[x] = 1
    if x == y:
        answer.append(count)
    for i in range(1, n+1):
        if graph[x][i] == 1 and visited[i] == 0:
            dfs(i, y, count)

dfs(p1, p2, count)
if (len(answer) == 0):
    print(-1)
else:
    print(answer[0] -1)
        


