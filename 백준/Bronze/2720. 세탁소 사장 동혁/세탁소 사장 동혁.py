T = int(input())
C =[]

for i in range(0,T):
    C.append(int(input()))

for i in range(T):
    coins = []
    coins.append(C[i]//25)
    temp = C[i]%25
    coins.append(temp//10)
    temp = temp%10
    coins.append(temp//5)
    temp = temp%5
    coins.append(temp)
    i+=1
    print(*coins)