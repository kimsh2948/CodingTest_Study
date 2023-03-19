import heapq

def solution(N, coffee_times):
    heap = [[0, i] for i in range(N)]
    heapq.heapify(heap)
    answer = []
    
    for time in coffee_times:
        end_time, idx = heapq.heappop(heap)
        end_time += time
        heapq.heappush(heap, [end_time, idx])
        answer.append(idx+1)
    
    return answer

N = 3
coffee_times = [4, 2, 2, 5 ,3]

print(solution(N, coffee_times))