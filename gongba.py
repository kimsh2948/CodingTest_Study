import math

count = int(input())

for i in range(count):
    a, b = map(int, input().split())
    print(math.lcm(a, b))