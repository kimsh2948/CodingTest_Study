s = input()
result = ""

for i in s:
    if 'A' <= i <= 'Z':
        i = ord(i) + 13
        if i > 90:
            i -= 26
        result += chr(i)
    elif 'a' <= i <= 'z':
        i = ord(i) + 13
        if i > 122:
            i -= 26
        result += chr(i)
print(result)
