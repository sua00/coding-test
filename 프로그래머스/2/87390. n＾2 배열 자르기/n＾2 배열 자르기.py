# n의 범위가 너무 크기 때문에 n*n 배열 만들면 안됨
# 각 칸 자체의 규칙을 찾아야함 : 행, 열 중 더 큰 값 +1

def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1): 
        row = i //n
        col = i%n
        
        answer.append(max(row, col)+1)
    return answer