#구현.. 아이디어가 중요....
def solution(n, left, right):
    answer = []
    #인덱스로 행렬을 치환했을때.. 몫이 행, 나머지가 열이 됨
    for i in range(left, right+1):
        row = i // n
        col = i % n
        
        #각 인덱스에 해당하는 값은 행, 렬 중 큰 값의 +1
        answer.append(max(row, col)+1)
    return answer