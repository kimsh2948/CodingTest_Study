def solution(A):
    turn = [0] * len(A)
    shine = [0] * len(A)
    answer = 0
    for i in range(len(A)):
        turn[A[i]-1] = 1
        if (shine[A[i]-2]) == 1:
            shine[A[i]-1] = 1
            answer += 1
        for j in range(0, i+1):
            if turn[j] == 1:
                shine[j] = 1
    answer += 1
    return answer

b = [2, 1, 3 ,5, 4]
print(solution(b))