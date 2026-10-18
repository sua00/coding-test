def solution(elements):

    n = len(elements)
    arr = elements *2
    result = set()
    
    for start in range(n): #0,1,2,3,4
        total = 0
        
        for length in range(1,n+1):
            total += arr[start+length-1]
            result.add(total)
    
    return len(result)