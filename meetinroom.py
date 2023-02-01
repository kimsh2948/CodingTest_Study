n = int(input())

meeting_time = []
for i in range(n):
    s, e = map(int, input().split())
    meeting_time.append([s, e])

meeting_time.sort(key=lambda x:x[0])
meeting_time.sort(key=lambda x:x[1])

end_time = 0
count = 0
for meet in meeting_time:
    if meet[0] >= end_time:
        count += 1
        end_time = meet[1]

print(count)