import math

def PrimeNum(i):
    if i <= 1:
        return False
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            return False
    return True

a, b = map(int, input().split())
prime = 0

for i in range(a, b+1):
    if PrimeNum(i):
        print(i)
    

