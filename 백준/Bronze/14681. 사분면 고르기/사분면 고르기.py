nums = []
for _ in range(2):
    nums.append(int(input()))
if nums[0]*nums[1] > 0:
    if nums[0] < 0:
        print(3)
    else:
        print(1)
else :
    if nums[0] < 0:
        print(2)
    else :
        print(4)
    