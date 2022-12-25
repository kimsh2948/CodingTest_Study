from collections import deque

n, k = map(int, input().split())

visited = [0] * (100001)

def bfs(n, k):
    queue = deque([n])
    while queue:
        v = queue.popleft()
        if v == k:
            print(visited[v])
            break
        for i in (v + 1, v - 1, 2 * v):
            if 0 < i <= 100000 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[v] + 1

bfs(n, k)
