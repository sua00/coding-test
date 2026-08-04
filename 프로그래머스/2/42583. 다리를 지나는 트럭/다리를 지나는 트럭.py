from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    trucks = deque(truck_weights)
    time = 0
    on_bridge = 0
    
    while trucks:
        time +=1
        on_bridge -= bridge.popleft()
        
        if on_bridge + trucks[0] <= weight:
            t= trucks.popleft()
            bridge.append(t)
            on_bridge += t
        else:
            bridge.append(0)
            
    return time+bridge_length