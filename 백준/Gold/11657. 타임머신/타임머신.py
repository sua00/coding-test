import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 수, 간선 수
n, m = map(int, input().split())
start = 1

# 간선 정보 저장 (u → v, cost)
edges = []
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


def bellman_ford(start):
    distance[start] = 0

    # V-1번 반복
    for i in range(n-1):
        for u, v, cost in edges:
            if distance[u] != INF and distance[v] > distance[u] + cost:
                distance[v] = distance[u] + cost

    # 음수 사이클 확인
    for u, v, cost in edges:
        if distance[u] != INF and distance[v] > distance[u] + cost:
            return True  # 음수 사이클 존재

    return False


# 실행
has_negative_cycle = bellman_ford(start)

if has_negative_cycle:
    print(-1)
else:
    for i in range(2, n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])