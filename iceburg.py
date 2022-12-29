import sys
from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

def bfs(x, y):
    queue = deque([x, y])
    visited[x][y] = 1
    sealist = []
    while queue:
        x = queue.popleft()
        y = queue.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and visited[nx][ny] == 0:
                    queue.append(nx)
                    queue.append(ny)
                    visited[nx][ny] = 1
                elif graph[nx][ny] == 0:
                    sea += 1
        if sea > 0:
            sealist.append((x, y, sea))
    for x, y, sea in sealist:
        graph[x][y] = max(0, graph[x][y] - sea)
    return 1

year = 0
while True:
    visited = [[0] * m for _ in range(n)]
    count = 0
    result = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == 0:
                count += bfs(i, j)
                result.append(count)
    if len(result) > 1:
        print(year)
        break
    year += 1

if count < 2:
    print(0)