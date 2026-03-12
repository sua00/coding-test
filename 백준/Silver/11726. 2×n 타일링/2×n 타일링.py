import math

width = int(input())
height = 2

temp = width//2
answer = 0

for i in range (0, temp+1):
    if i == 0:
        answer += 1
    else :
        num_one = width - 2*i
        num_two = i
        nums = width - i
        answer += math.factorial(nums)//(math.factorial(num_one)*math.factorial(num_two))
answer %= 10007
        
print(int(answer))