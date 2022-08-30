from itertools import permutations

def is_prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    num_list = []
    for i in range(2, len(numbers)):
        num_list.extend(list(permutations(numbers, i)))
        
    num_list = list(map(int, num_list))
    for i in num_list:
        if is_prime_number(i):
            answer += 1
    
    return answer

print