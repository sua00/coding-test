def solution(answers):
    answer = []
    pattern_1 = [1,2,3,4,5]
    pattern_2 = [2,1,2,3,2,4,2,5]
    pattern_3 = [3,3,1,1,2,2,4,4,5,5]
    
    score= [0,0,0]
    
    for i in range(len(answers)):
        if answers[i] == pattern_1[i%len(pattern_1)]:
            score[0] += 1
        if answers[i] == pattern_2[i%len(pattern_2)]:
            score[1] += 1    
        if answers[i] == pattern_3[i%len(pattern_3)]:
            score[2] += 1  
            
    max_score = max(score)
    
    for i in range(len(score)):
        if score[i] == max_score:
            answer.append(i+1)
    return answer