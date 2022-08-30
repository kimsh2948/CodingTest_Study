alpha = input()
alpha_lst = [0] * 26

for i in alpha:
    alpha_lst[ord(i) - ord('a')] += 1


for i in range(len(alpha_lst)):
    print(alpha_lst[i], end=' ')