n = int(input())
for _ in range(n):
    cnt = 0
    i, j = map(int, input().split()) #각 테스트케이스 마다 실행
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    a_idx = 0
    b_idx = 0

    while a_idx < i and b_idx < j:
        if A[a_idx] > B[b_idx]:
            cnt += i - a_idx
            b_idx +=1
        else:
            a_idx += 1
    print(cnt)  