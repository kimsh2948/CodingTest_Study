from collections import deque

def bfs(v, n, graph):
    queue = deque([v])
    visited.append((graph[v][0], graph[v][1]))
    while queue:
        v = queue.popleft()
        if v == n+1:
            break
        dist = abs(graph[v+1][0] - graph[v][0]) + abs(graph[v+1][1] - graph[v][1])
        print(dist)
        if dist // 20 > 50:
            print("sad")
            return
        for i in range(n+1):
            x = graph[v+1][0]
            y = graph[v+1][1]
            if (x, y) not in visited:
                queue.append(v+1)
                visited.append((x, y))
        print(visited)
    print("happy")

t = int(input())

for i in range(t):
    graph = []
    n = int(input())
    for j in range(n+2):
        graph.append(list(map(int, input().split())))
    visited = []
    bfs(0, n, graph)

