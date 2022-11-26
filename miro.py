from collections import deque

n, m = map(int, input().split())

graph = []
count = 0

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]

visited = [[0] * m for i in range(n)]

visited[0][0] = 1

def bfs(x, y):
    queue = deque([x, y])
    while queue:
        x = queue.popleft()
        y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append(nx)
                    queue.append(ny)
    return visited[n-1][m-1]
print(bfs(0, 0))

