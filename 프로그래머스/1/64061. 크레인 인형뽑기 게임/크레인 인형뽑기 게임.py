def solution(board, moves):
    answer = 0
    # [[0, 0, 0, 0, 0]
    #  [0, 0, 0, 0, 0]
    #  [0, 0, 5, 0, 0]
    #  [0, 2, 4, 4, 2]
    #  [0, 5, 1, 3, 1]] [1, 5, 3, 5, 1, 2, 1, 4]
    
    #[4,,2,4]
    #moves -> [n][1]
    stack= []
    
    for move in moves:
        doll =0
        col = move-1
        for row in range(len(board)):
            
            if board[row][col]!= 0:
                doll = board[row][col]
                board[row][col] = 0
                #print(doll)
                break
        
        if doll ==0:
            continue
        if stack and stack[-1] == doll:
            stack.pop()
            answer+=2
        else:
            stack.append(doll)
        
    
            
    return answer