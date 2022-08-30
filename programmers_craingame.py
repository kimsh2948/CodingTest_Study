def solution(board, moves):
    answer = 0
    bascket = []
    reverse = []
    
    for m in moves:
        for j in range(len(board)):
            if board[j][m-1] > 0:
                bascket.append(board[j][m-1])
                board[j][m-1] = 0
                if bascket[-1:] == bascket[-2:-1]:
                    bascket = bascket[:-2]
                    answer += 2
                break
            
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
result = solution(board, moves)
print(result)