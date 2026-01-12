#입력은 표준입력을 사용한다. 
#입력의 첫 번째 행에는 팀 수를 나타내는 양의 정수 n(1 ≤ n ≤ 5,000)이 주어진다. 
#그 다음 행에 학생 si 의 코딩 역량 w(si)를 나타내는 2n개의 양의 정수가 공백으로 분리되어 주어진다 (1 ≤ w(si) ≤ 100,000). 
#학생들의 코딩 역량은 모두 다르다. 즉, i ≠ j이면 w(si) ≠ w(sj)이다.

n = int(input())
team = 2*n
levels = list(map(int, input().split()))

levels = sorted(levels)
levels_sum = []

for i in range(0,n,1):
    temp = levels[i] + levels[team-1-i]
    levels_sum.append(temp)
    
print(min(levels_sum))
    
    