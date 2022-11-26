from collections import deque
import sys
sys.setrecursionlimit(10**7)

n = int(input())
m = int(input())

graph = [[0]* (n+1) for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [0] * (n+1)

def dfs(v):
    visited[v] = 1
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = 1
    count = 0
    while queue:
        v = queue.popleft()
        count = count + 1
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
            
    return count - 1

print(bfs(1))
visited = [0] * (n+1)
dfs(1)
print(sum(visited)-1)