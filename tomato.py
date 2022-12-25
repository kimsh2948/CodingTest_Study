from collections import deque

m, n, h = map(int, input().split())

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0 ,0]
dz = [0, 0, 0, 0, -1, 1]

graph = []
tmp = []

for i in range(n):
    for j in range(h):
        tmp.append(list(map(int, input().split())))
    graph.append(tmp)

def bfs(x, y, z):
    count = 0
    queue = deque([x, y, z])
    while queue:
        x = queue.popleft()
        y = queue.popleft()
        z = queue.popleft()
        count += 1
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < x and 0 <= ny < y and 0 <= nz < z:
                if graph[nx][ny][nz] == 0 and graph[x][y][z] == 1:
                    queue.append(nx, ny, nz)
                    graph[nx][ny][nz] = 1
    return count

count = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[k][j][i] == 1
                count = bfs(k, j, i)

print(count)




