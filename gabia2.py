def solution(N, coffee_times):
    answer = []
    ord_list = list(range(1, len(coffee_times) + 1))
    time_list = coffee_times[:]
    
    m_list = [] 
    k_list = list(zip(ord_list, time_list))
    
    while k_list or m_list:
        while len(m_list) < N and k_list:
            m_list.append(k_list.pop(0))
        
        for i in range(len(m_list)):
            m_list[i] = (m_list[i][0], m_list[i][1] - 1)
            if m_list[i][1] == 0:
                answer.append(m_list[i][0])
        
        m_list = [(order, time) for order, time in m_list if time > 0]
        
    return answer

N = 3
coffee_times = [4, 2, 2, 5 ,3]

print(solution(N, coffee_times))