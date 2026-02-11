# 첫 번째 배열
n = int(input())
arr1 = list(map(int, input().split()))

# 두 번째 배열
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid-1
        else :
            start = mid+1
    return 0

result = []

for i in arr2:
    result.append(binary_search(arr1, i, 0, n-1))

print(*result)