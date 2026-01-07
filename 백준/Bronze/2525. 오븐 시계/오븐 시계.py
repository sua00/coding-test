current_time = list(map(int, input().split()))
duration  = int(input())
current_minute = current_time[0] * 60 + current_time[1]
due_time = current_minute + duration
due_hour = due_time // 60
due_minute = due_time % 60

if due_hour >= 24:
    due_hour -= 24

print(due_hour, due_minute)
