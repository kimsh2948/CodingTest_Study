def solution(new_id):
    answer = ''
    new_word = []
    new_id = new_id.lower()
    new_id = list(new_id)
    for id in new_id:
        if id.isalpha() or id.isdigit() or id == '-' or id == '_' or id == '.':
            new_word.append(id)
    print(new_word)
    new_word = list(remove(new_word))
    print(new_word)
    if new_word[0] == '.':
        new_word.pop(0)
    if new_word[-1] == '.':
        new_word.pop()

    for i in range(len(new_word)):
        if new_word[i] == ' ':
            new_word[i] = "a"
    if len(new_word) >= 16:
        new_word = new_word[0:15]
    if new_word[-1] == '.':
        new_word.pop()
    while len(new_word) <= 2:
        new_word.append(new_word[-1])
    answer = "".join(new_word)
    return answer

def remove(new_word):
    result = []
    for i in range(0, len(new_word)-1):
        if new_word[i] == new_word[i-1]:
            if new_word[i] == '.':
                print(new_word)
                continue
        else:
            result.append(new_word[i])
    return result

new_id = "=.="
print(solution(new_id))