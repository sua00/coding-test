N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 그래프 구현
# 각 자리에서 어디로 이동을 하게 되는지
# (0,0) -> (1,0) 또는 (0,1)
# (0,1) -> (0,3) 또는 (2,1)
graph = {}

for r in range(N) : 
    for c in range(N):
        graph[(r,c)] = [] # (r,c) 에서 다음으로 이동할 좌판을 넣어준다
        
        jump = board[r][c] #발판에 적혀있는 숫자

        #오른쪽으로 이동할 겨웅
        nr, nc = r+jump, c
        if nr <= N-1 and nc<= N-1:
            graph[(r, c)].append((nr, nc))

        #밑으로 이동할 경우
        nr, nc = r, c+jump
        if nr <= N-1 and nc<= N-1:
            graph[(r, c)].append((nr, nc))

        # 도착 지점(-1)은 더 이상 이동 X 
        if jump == -1 :
            continue
            
#DFS 함수
def dfs(node):
    # 도착점에 도달한 경우
    if node == (N-1, N-1):
        return True

    visited.add(node)

    for next_node in graph[node]:
        if next_node not in visited:
            if dfs(next_node):
                return True

    return False

visited = set()

if dfs((0, 0)): #결과가 True가 나오면 
    print("HaruHaru")
else:
    print("Hing")
