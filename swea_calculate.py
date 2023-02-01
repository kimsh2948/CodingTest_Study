from collections import deque

t = int(input())

def bfs(n, m):
    queue = deque([n])
    visited[n] = 1
    while queue:
        n = queue.popleft()
        if n == m:
            return visited[n] - 1
        for i in (n+1, n-1, 2*n, n-10):
            if 0 <= i <= 1000000 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[n] + 1

result = []

for i in range(t):
    n, m = map(int, input().split())
    visited = [0] * 1000001
    result.append(bfs(n, m))

for i in range(len(result)):
    print("#" + str(i+1) + " " + str(result[i]))

