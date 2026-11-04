def solution(nums):
    answer = 0
    species = set(nums)
    
    if len(species) >= len(nums)//2:
        answer = len(nums)//2
    else:
        answer = len(species)
    return answer