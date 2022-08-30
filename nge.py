count = int(input())

arr = list(map(int, input().split()))
stack = []
start = arr[0]
j = 1

nge = -1

for i in range(count):
    while j < count:
        if arr[j] > arr[i]:
            nge_arr.append(arr[j])
            break
        j+=1
    j += 1
    

print(nge_arr)
        
    
    

