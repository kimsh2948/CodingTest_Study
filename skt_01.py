def solution(p):
    answer = [0] * len(p)
    for i in range(len(p)):
        if min(p) != p[i]:
            tmp = p[i]
            p[i] = p[p.index(min(p))]
            p[p.index(min(p))] = tmp
            answer[p.index(min(p))] += 1
    return answer

p = [2,5,3,1,4]
an = []
an = solution(p)
print(an)