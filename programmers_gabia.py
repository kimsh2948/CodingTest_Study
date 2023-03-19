import heapq

def solution(N, coffee_times):
    answer = []
    heap = []
    e_time = 0
    
    for i, cof_time in enumerate(coffee_times):
        if len(heap) < N:
            heapq.heappush(heap, (cof_time + e_time, i + 1))
        else:
            e_time, num = heapq.heappop(heap)
            answer.append(num)
            heapq.heappush(heap, (cof_time + e_time, i + 1))
    
    while heap:
        e_time, num = heapq.heappop(heap)
        answer.append(num)
    
    return answer

N = 3
coffee_times = [4, 2, 2, 5 ,3]

print(solution(N, coffee_times))