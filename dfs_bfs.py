from collections import deque

n, m, v = map(int, input().split())

graph = [[0] * (n+1)for i in range(n+1)]
for i in range(m):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1

visited1 = [0] * (n+1)
visited2 = [0] * (n+1)

def dfs(v):
    print(v, end=' ')
    visited1[v] = 1
    for i in range(1, n+1):
        if visited1[i] == 0 and graph[v][i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited2[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visited2[i] == 0 and graph[v][i]:
                visited2[i] = 1
                queue.append(i)

dfs(v)
print()
bfs(v)