count = int(input())

num_list = list(map(int, input().split()))
prime = 0

for i in num_list:
    check_ = 0
    if i <= 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            check_ += 1
    if check_ == 0:
        prime += 1

print(prime)
