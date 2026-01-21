n = int(input())
nums = []
str_ = []
for i in range(n):
    a,b = input().split(" ")
    nums.append(int(a))
    str_.append(b)

for i in range(n):
    ans = ''
    for j in range(len(str_[i])):
        ans += str_[i][j] * nums[i]
    print(ans)
    