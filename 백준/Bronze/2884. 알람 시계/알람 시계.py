goal_time = list(map(int, input().split()))
goal_minute = goal_time[0]*60+goal_time[1]

early_alarm = goal_minute - 45
early_hour = early_alarm//60
early_minute = early_alarm%60

if(early_hour < 0):
    early_hour = 23
print(early_hour, early_minute)