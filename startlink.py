from collections import deque

f, s, g, u, d = map(int, input().split())

visited = [0] * (f + 1)

def bfs(s, g):
    queue = deque([s])
    visited[s] = 1
    while queue:
        v = queue.popleft()
        if v == g:
            print(visited[v] - 1)
            return
        for i in (v + u, v - d):
            if 0 < i <= f and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[v] + 1
    print("use the stairs")

bfs(s, g)

