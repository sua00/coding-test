def solution(n, costs):
    answer = 0
    parents = []
    
    def find(parents, x):
        if parents[x] != x:
            parents[x] =find(parents, parents[x])
        return parents[x]
    
    def union(parents, a, b):
        a= find(parents, a)
        b = find(parents, b)
        
        if a < b :
            parents[b] =a
        else:
            parents[a]=b
    
    # 먼저 비용순으로 정리
    costs = sorted(costs, key = lambda x: x[2])
    answer, cnt = 0,0
                   
    # 부모노드 모두 넣기
    for i in range(n):
        parents.append(i)
    
    for a, b, cost in costs:
        if find(parents, a) != find(parents, b):
            union(parents,a,b)
            
            answer += cost
    
    return answer