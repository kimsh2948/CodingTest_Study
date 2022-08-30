import sys

while(True):
    result = [0] * 4
    word = sys.stdin.readline().rstrip('\n')

    if not word:
        break
    
    for j in word:
        if j.isalpha():
            if j.isupper():
                result[1] += 1
            else:
                result[0] += 1
        else:
            if j == ' ':
                result[3] += 1
            else:
                result[2] += 1
    for r in range(len(result)):
        print(result[r], end=' ')
    print()
