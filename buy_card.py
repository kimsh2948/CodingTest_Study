count = int(input())
card = list(map(int, input().split()))
card.insert(0, 0)
list = [0] * (count+1)

for i in range(1, count+1):
    for j in range(1, i+1):
        list[i] = max(list[i], list[i-j] + card[j])

print(list[count])
            
