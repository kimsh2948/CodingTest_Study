n = input()
len = len(n)
result = 0
for i in range(1, len):
    result += 9 * (10 ** (i-1)) * i

result += (int(n) - (10 ** (len-1))+1) * len
print(result)