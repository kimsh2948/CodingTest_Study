count = int(input())
g_word = 0

for i in range(count):
    word = input()
    check = 0
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            new_word = word[j+1:]
            if word[j] in new_word:
                check += 1
    if check == 0:
        g_word += 1

print(g_word)
        
