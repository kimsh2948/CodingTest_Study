tall = []
result = []

for i in range(9):
    tall.append(int(input()))

sum_tall = sum(tall)

for i in range(9):
    for j in range(i+1, 9):
        if sum_tall - (tall[i] + tall[j]) == 100:
            num1, num2 = tall[i], tall[j]
            tall.remove(num1)
            tall.remove(num2)
            break
    if(len(tall)<9):
        break

result = sorted(tall)

for i in range(0, len(result)):
    print(result[i])
