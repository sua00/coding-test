import math

def solution(fees, records):
    answer = []
    base_time, base_fee, unit_time, unit_fee = fees
    
    in_time = {}
    total_time = {}
    
    def hour_to_min(time):
        h, m = map(int, time.split(':'))
        return h*60+m
    
    for record in records:
        time, car, status = record.split(' ')
        minutes = hour_to_min(time)
        
        if status == 'IN':
            in_time[car] = minutes
        else:
            parking_time = minutes- in_time[car]
            total_time[car] = total_time.get(car,0) +parking_time
        
            del in_time[car]
    
    for car, start in in_time.items():
        parking_time = hour_to_min('23:59')-start
        total_time[car] = total_time.get(car,0)+parking_time
        
    for car in sorted(total_time):
        time = total_time[car]
        
        if time <= base_time:
            answer.append(base_fee)
        else:
            extra = time-base_time
            fee = base_fee + math.ceil(extra/unit_time)*unit_fee
            answer.append(fee)
    return answer