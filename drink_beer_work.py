from collections import deque

def bfs(x, y):
    queue = deque([x, y])
    


t = int(input())
for i in range(t):
    graph = []
    n = int(input())
    for j in range(n):
        x, y = map(int, input().split())
        graph.append(x, y)
    


