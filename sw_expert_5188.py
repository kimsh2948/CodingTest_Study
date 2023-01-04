from collections import deque

t = int(input())
answer = []

def bfs(x, y, visited):
    queue = deque([x, y])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = graph[x][y]
    while queue:
        x = queue.popleft()
        y = queue.popleft()
        if x == n-1 and y == n-1:
            print(visited)
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 or visited[nx][ny] > graph[nx][ny] + visited[x][y]:
                    queue.append(nx)
                    queue.append(ny)
                    visited[nx][ny] = graph[nx][ny] + visited[x][y]

for _ in range(t):
    n = int(input())
    graph = []
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        graph.append(list(map(int, input().split())))
    answer.append(bfs(0, 0, visited))

for i in range(t):
    print("#" + str(i+1) + " " + str(answer[i]))

