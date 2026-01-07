# 시험 본 과목의 개수
n = int(input())

# 세준이의 현재 성적 리스트
scores = list(map(int, input().split()))

# 최고 점수
high_score = max(scores)

# 점수 조정
new_scores = [(s / high_score) * 100 for s in scores]

# 새로운 평균
avg = sum(new_scores) / n

print(avg)
