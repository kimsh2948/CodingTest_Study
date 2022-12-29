from collections import deque

n, m = map(int, input().split())

r, c, d = map(int, input().split())

graph = []
if d == 0:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
elif d == 1:
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
elif d == 2:
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
elif d == 3:
    dx = [0, -1, 1, 0]
    dy = [1, 0, 0, -1]


clear = [[0] * m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs(c, r, d):
    queue = deque([c, r])
    clear[c][r] = 1
    while queue:
        c = queue.popleft()
        r = queue.popleft()
        for i in range(4):
            nx = c + dx
            ny = r + dy
            if graph[nx][ny] == 0 and clear[nx][ny] == 0:
                queue.append(nx)
                queue.append(ny)
                clear[nx][ny] = 1
    


