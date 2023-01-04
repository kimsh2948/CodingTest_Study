from collections import deque

n, k = map(int, input().split())

visited = [0] * 100001
check = [0] * 100001

def path(v):
    result = []
    tmp = v
    for i in range(visited[v]):
        result.append(tmp)
        tmp = check[tmp]
    print(' '.join(map(str, result[::-1])))

def bfs(n, k):
    queue = deque([n])
    visited[n] = 1
    while queue:
        v = queue.popleft()
        if v == k:
            print(visited[v] - 1)
            path(v)
            return
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= 100000 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[v] + 1
                check[i] = v

bfs(n, k)
            

    
