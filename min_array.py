n = int(input())
arr = list(map(int, input().split()))

result = []
result.append(arr[0])
for i in range(1, len(arr)):
    if result[-1] < arr[i]:
        result.append(arr[i])

print(len(result))
