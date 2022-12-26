from collections import deque
import sys

n = int(input())

graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

max_num = 0

for i in range(n):
    for j in range(n):
        if max_num < graph[i][j]:
            max_num = graph[i][j]

def bfs(x, y, visited, rain):
    queue = deque([x, y])
    while queue:
        x = queue.popleft()
        y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > rain and visited[nx][ny] == 0:
                    queue.append(nx)
                    queue.append(ny)
                    visited[nx][ny] = 1

result = 0

for wid in range(2, max_num+1):
    rain = wid
    visited = [[0] * (n)for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > rain and visited[i][j] == 0:
                bfs(i, j, visited, rain)
                count += 1
                visited[i][j] = 1
    if result < count:
        result = count

print(result)


