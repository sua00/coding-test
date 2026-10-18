def solution(n):
    answer = 0
    cnt2 = 0
    def count_1(s:str): #n을 2진수로 변화시킨 자릿수에 비례하므로 O(logN)
        count = 0
        for i in s:
            if i == '1':
                count+=1
        return count
    
    cnt1 = count_1(bin(n)) #bin: O(logN)
    n = n+1
    
    while count_1(bin(n)) != cnt1: #최대 : O(N)
        n = n+1
        
    return n