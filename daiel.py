alpha = input()
count = 0

for a in alpha:
    if a in "ABC":
        count += 3
    elif a in "DEF":
        count += 4
    elif a in "GHI":
        count += 5
    elif a in "JKL":
        count += 6
    elif a in "MNO":
        count += 7
    elif a in "PQRS":
        count += 8
    elif a in "TUV":
        count += 9
    elif a in "WXYZ":
        count += 10

print(count)
    
