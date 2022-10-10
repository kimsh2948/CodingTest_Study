from collections import deque
import sys

def bfs(graph, v, visited):
    visited[v] = True
    queue = deque([v])

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for e in graph:
    e.sort()

visited = [False] * len(graph)

dfs(graph, v, visited)
print()

visited = [False] * len(graph)

bfs(graph, v, visited)

    
