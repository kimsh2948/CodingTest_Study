import sys

word = input()
count = int(input())

word_stack = list(word)
temp_stack = []

for i in range(count):
    cur = sys.stdin.readline().split()
    if cur[0] == 'D' and temp_stack:
        word_stack.append(temp_stack.pop())
    elif cur[0] == 'L' and word_stack:
        temp_stack.append(word_stack.pop())
    elif cur[0] == 'B' and word_stack:
        word_stack.pop()
    elif cur[0] == 'P':
        word_stack.append(cur[1])

print("".join(word_stack + list(reversed(temp_stack))))