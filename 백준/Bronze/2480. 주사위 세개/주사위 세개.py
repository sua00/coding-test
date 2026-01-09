"""
같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다
"""
nums = list(map(int, input().split()))
if nums[0] == nums[1] == nums[2]:
    print(nums[0]*1000+10000)
elif (nums[0]==nums[1]) or (nums[0] == nums[2]) or (nums[1]==nums[2]):
    a = sorted(nums)[1]
    print(1000+a*100)
else:
    a = sorted(nums)[2]
    print(a*100)