import sys

word_count = int(sys.stdin.readline().strip())

for i in range(word_count):
    word_arr = []
    word = input()
    word_arr = word.split()
    for rew in word_arr:
        print(rew[::-1], end=' ')


