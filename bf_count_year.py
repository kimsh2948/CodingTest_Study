e, s, m = map(int, input().split())
e1, s1, m1, count = 1, 1, 1, 1

while True:
    if e1==e and s1== s and m1 == m:
        break
    e1 +=1
    s1 += 1
    m1 += 1
    count += 1
    if e1 >= 16: 
        e1 -= 15
    if s1 >= 29: 
        s1 -= 28
    if m1 >= 20: 
        m1 -= 19

print(count)