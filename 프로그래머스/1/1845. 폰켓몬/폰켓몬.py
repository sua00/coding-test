def solution(nums):
    answer = 0
    mon = set()
    for i in nums:
        mon.add(i)
    answer = min(len(mon),len(nums)/2)
    return answer