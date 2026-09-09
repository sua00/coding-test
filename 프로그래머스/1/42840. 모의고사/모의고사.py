def solution(answers):
    answer = []
    stu1 = [1,2,3,4,5] #5
    stu2 = [2,1,2,3,2,4,2,5] #8
    stu3 = [3,3,1,1,2,2,4,4,5,5] #10
    score1,score2,score3 = 0,0,0
    scores=[0,0,0]
    
    for i in range(len(answers)):
        if answers[i] == stu1[i%5]:
            scores[0] = scores[0]+1
        if answers[i] == stu2[i%8]:
            scores[1] = scores[1]+1
        if answers[i] == stu3[i%10]:
            scores[2] = scores[2]+1
    max_score = max(scores)
    
    for i in range(len(scores)):
        if max_score == scores[i]:
            answer.append(i+1)
    return answer