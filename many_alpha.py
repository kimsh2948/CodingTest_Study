word = input()

word = word.upper()

alpha = [0] * 26

for sp in word:
    alpha[ord(sp) - ord("A")] += 1

max_num = alpha[0]
max_index = 0
dual = 0

for i in range(1, len(alpha)):
    if max_num < alpha[i]:
        max_num = alpha[i]
        max_index = i
        dual = 0
    elif max_num == alpha[i]:
        dual = 1
    
if dual == 1:
    print("?")
else:
    print(chr(max_index + ord("A")))