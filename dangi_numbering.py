from collections import deque

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[0] * n for _ in range(n)]

def bfs(x, y):
    queue = deque([x, y])
    visited[x][y] = 1
    res = 1
    while queue:
        x = queue.popleft()
        y = queue.popleft()
        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    queue.append(nx)
                    queue.append(ny)
                    visited[nx][ny] = 1
                    res += 1
    return res

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            result.append(bfs(i, j))
result.sort()
print(len(result))
for res in result:
    print(res)



