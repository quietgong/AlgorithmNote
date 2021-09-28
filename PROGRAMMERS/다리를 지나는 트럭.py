def solution(bridge_length, weight, truck_weights):
    ans = 0
    q=[0]*bridge_length
    while len(q):
        ans+=1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return ans

# 지나는 다리를 q로 만들어서 생각한다.
# 예) 다리의 길이:3 -> 000