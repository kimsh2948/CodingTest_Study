t = int(input())

for j in range(t):
    num = int(input())
    result = []

    result.append(0)
    result.append(1)
    result.append(2)
    result.append(4)

    for i in range(4, num+1):
        result.append(result[i-1] + result[i-2] + result[i-3])
    print(result[num])
