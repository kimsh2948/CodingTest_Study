import sys
from collections import deque

def bfs(x, y):
    queue = deque([x, y])
    visited[x][y] = 1
    print(graph)
    while queue:
        x = queue.popleft()
        y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append(nx)
                    queue.append(ny)
                    visited[nx][ny] = 1
    return 1

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    result = 0
    visited = [[0] * h for _ in range(w)]
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]
    for i in range(h):
        graph.append(list(map(int, input().split())))
    for i in range(w):
        for j in range(h):
            if graph[i][j] == 1 and visited[i][j] == 0:
                result += bfs(i, j)
    print(result)