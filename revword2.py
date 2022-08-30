#다시 풀어볼것
word_list = list(input())
st = 0

for i in range(len(word_list)):
    if word_list[i] == '<':
        while word_list[i] == '>':
            i += 1
    elif word_list[i].isalnum():
        st = i
        while i < len(word_list[i]) and word_list[i].isalnum():
            i += 1
        tmp = word_list[st:i]
        tmp.reverse()
        word_list[st:i] = tmp
    else:
        i += 1

print(''.join(word_list))



        