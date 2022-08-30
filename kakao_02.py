def solution(queue1, queue2):
    answer = -1
    count_1 = 0
    count_2 = 0
    tmp_queue1 = queue1
    tmp_queue2 = queue2

    for i in range(len(queue1)):
        queue2.append(queue1.pop(0))
        if (sum(queue1) == sum(queue2)):
            answer = count_1
            break
        count_1 += 1
    
    for i in range(len(tmp_queue2)):

    return answer