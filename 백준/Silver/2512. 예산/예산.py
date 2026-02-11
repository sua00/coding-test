n = int(input())
arr1 = list(map(int, input().split()))
max_sum = int(input())

left = 0
right = max(arr1)

while left <= right:
    mid = (left + right) // 2
    total = sum(min(x, mid) for x in arr1)

    if total <= max_sum:
        left = mid + 1
    else:
        right = mid - 1

print(right)