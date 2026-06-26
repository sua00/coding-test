# 정수들에 플러스 혹은 마이너스를 붙여서 타겟넘버를 만들어라
# 타겟넘버를 만드는 경우의 수를 return하라
# 모든 +/- 조합을 다 만들어보고, 그 결과가 target이 되는 조합이 몇 개인지 세는 문제입니다.
#주어진 제약사항 : 주어지는 숫자의 개수는 20개 이하 -> 만들어질 수 있는 조합은 100만개 정도(2의 20승)
# 이러면 부르트포스(모든 경우의 수 확인)가능하긴함 -> 그러나 for문을 몇번을 중첩해야하는지 알 수가없음(최대20회)
# 따라서 dfs의 재귀 방식을 사용해야함
def solution(numbers, target):
    answer = 0
    
    def dfs(index, current_sum):
        if index == len(numbers): #모든 숫자에 대해 +/-검증을 한 경우
            if current_sum == target: #타겟넘버에 도달했는지 확인
                nonlocal answer #선언
                answer +=1
            return
        #index가 끝이 아니라면?
        dfs(index+1, current_sum + numbers[index])
        dfs(index+1, current_sum - numbers[index])
    dfs(0,0)
    return answer
                
            