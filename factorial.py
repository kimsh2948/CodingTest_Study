def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n-1)

n = int(input())

print(facto(n))