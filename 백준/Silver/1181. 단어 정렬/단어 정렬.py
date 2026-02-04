import sys
input = sys.stdin.readline

n = int(input())
strings = set()

for _ in range(n):
    strings.add(input().strip())
    
list_strings = list(strings)
list_strings.sort(key = lambda x: (len(x),x))

for i in list_strings:
    print(i)