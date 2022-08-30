def solution(survey, choices):
    i = 0
    R, T, F, C, M, J, A, N = 0, 0 ,0, 0, 0, 0, 0, 0
    result = []
    answer = ''

    for case in survey:
        if case == "RT":
            if choices[i] < 4:
                if choices[i] == 1:
                    R += 3
                elif choices[i] == 2:
                    R += 2
                elif choices[i] == 3:
                    R += 1
            elif choices[i] > 4:
                T += choices[i] - 4
        elif case == "TR":
            if choices[i] < 4:
                if choices[i] == 1:
                    T += 3
                elif choices[i] == 2:
                    T += 2
                elif choices[i] == 3:
                    T += 1
            elif choices[i] > 4:
                R += choices[i] - 4
        elif case == "FC":
            if choices[i] < 4:
                if choices[i] == 1:
                    F += 3
                elif choices[i] == 2:
                    F += 2
                elif choices[i] == 3:
                    F += 1
            elif choices[i] > 4:
                C += choices[i] - 4
        elif case == "CF":
            if choices[i] < 4:
                if choices[i] == 1:
                    C += 3
                elif choices[i] == 2:
                    C += 2
                elif choices[i] == 3:
                    C += 1
            elif choices[i] > 4:
                F += choices[i] - 4
        elif case == "MJ":
            if choices[i] < 4:
                if choices[i] == 1:
                    M += 3
                elif choices[i] == 2:
                    M += 2
                elif choices[i] == 3:
                    M += 1
            elif choices[i] > 4:
                J += choices[i] - 4  
        elif case == "JM":
            if choices[i] < 4:
                if choices[i] == 1:
                    J += 3
                elif choices[i] == 2:
                    J += 2
                elif choices[i] == 3:
                    J += 1
            elif choices[i] > 4:
                M += choices[i] - 4
        elif case == "AN":
            if choices[i] < 4:
                if choices[i] == 1:
                    A += 3
                elif choices[i] == 2:
                    A += 2
                elif choices[i] == 3:
                    A += 1
            elif choices[i] > 4:
                N += choices[i] - 4
        elif case == "NA":
            if choices[i] < 4:
                if choices[i] == 1:
                    N += 3
                elif choices[i] == 2:
                    N += 2
                elif choices[i] == 3:
                    N += 1
            elif choices[i] > 4:
                A += choices[i] - 4
        i += 1
    if R >= T:
        result.append("R")
    else:
        result.append("T")
    if C >= F:
        result.append("C")
    else:
        result.append("F")
    if J >= M:
        result.append("J")
    else:
        result.append("M")
    if A >= N:
        result.append("A")
    else:
        result.append("N")
    
    answer = "".join(result)
    return answer