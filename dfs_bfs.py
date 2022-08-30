count = int(input())

graph = []
for i in range(count):
    graph.append(list(map(int, input().split())))

stack = []

while graph:
    
