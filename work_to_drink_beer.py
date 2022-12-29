from collections import deque

def bfs(v, n, graph, f_x, f_y):
    queue = deque([v])
    visited.append(graph[0])
    while queue:
        x, y = queue.popleft()
        if v == n+1:
            break
        dist = abs(graph[v+1][0] - graph[v][0]) + abs(graph[v+1][1] - graph[v][1])
        if dist // 20 > 50:
            print("sad")
            return
        for i in range(n+1):
            x = graph[v+1][0]
            y = graph[v+1][1]
            if (x, y) not in visited:
                queue.append(v+1)
                visited.append((x, y))
    print("happy")

t = int(input())

for i in range(t):
    graph = []
    n = int(input())
    for j in range(n+1):
        x, y = map(int, input().split())
        graph.append((x, y))
    f_x, f_y = map(int, input().split())
    visited = []
    bfs(0, n, graph, f_x, f_y)

