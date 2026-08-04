from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    trucks = deque(truck_weights)
    time = 0
    on_bridge = 0
    
    while trucks:
        time +=1
        b = bridge.popleft()
        on_bridge -= b
        
        if on_bridge + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            on_bridge += truck
        else:
            bridge.append(0)
            
    time = time + bridge_length
    return time