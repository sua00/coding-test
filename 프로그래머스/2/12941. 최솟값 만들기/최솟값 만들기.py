def solution(A,B):
    answer = 0

    #곱의 합이 최소가 되려고 하려면 한 배열에서의 최소와 한 배열에서의 최대가 곱해져야함
    A.sort()
    B.sort()
    num1, num2 = 0, 0

    for i in range(len(A)):
        num1 += A[i] * B[-1-i]
        num2 += A[-1-i]*B[i]
    
    answer = min(num1, num2)
    return answer