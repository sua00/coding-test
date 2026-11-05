def solution(answers):
    answer = []
    stu1 = [1,2,3,4,5] #5
    stu2 = [2,1,2,3,2,4,2,5] #8
    stu3 = [3,3,1,1,2,2,4,4,5,5] #10
    cor1, cor2, cor3 = 0,0,0
    
    for i in range(len(answers)):
        if answers[i] == stu1[i%5]:
            cor1+=1
        if answers[i] == stu2[i%8]:
            cor2+=1
        if answers[i] == stu3[i%10]:
            cor3+=1
            
    score = [cor1,cor2,cor3]
    max_score = max(score)
    
    for i in range(3):
        if score[i] == max_score:
            answer.append(i+1)
            
    return answer