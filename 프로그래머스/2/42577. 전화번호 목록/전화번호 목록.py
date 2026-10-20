
def solution(phone_book):
    
    phone_book.sort()

    current = phone_book[0]
    
    for i in range(1,len(phone_book)):
        if len(phone_book[i]) >= len(current): #앞의 단어가 뒷 단어 보다 짧으면 비교 시작
            same = True
            
            for j in range(len(current)):
                if current[j] != phone_book[i][j]:
                    same = False
                    current = phone_book[i]
                    break
                
            if same:
                return False
                    
        current = phone_book[i]
            
                
            
    return True