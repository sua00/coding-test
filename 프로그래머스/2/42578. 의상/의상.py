def solution(clothes):
    #print(clothes)
    answer = 1
    closet = {}
    for c in clothes:
        closet[c[1]] = closet.get(c[1],())+(c[0],)
    
    for i in closet:
        answer *= (len(closet[i])+1)
        
    answer -=1
    return answer
#     if len(closet)>1:
#         for i in closet:
#             answer += len(closet[i]) #의상 종류 하나씩만
#             temp *= len(closet[i]) #모든 의상 종류 다 쓸 때
            
#         answer += temp
#     else:
#         for i in closet:
#             answer += len(closet[i]) #의상 종류 하나일 때
#     #print(answer)
#     return answer
# #     print(temp)
# #     print(answer)
    
# #     for i in closet:
# #         print(i)
# #         print(len(closet[i]))
    
    