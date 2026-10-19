def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)

    def dfs(fatigue, count):
        nonlocal answer

        # 현재까지 탐험한 최대 던전 수 저장
        answer = max(answer, count)

        for i in range(len(dungeons)):

            # 방문하지 않았고, 피로도가 충분한 경우
            if not visited[i] and dungeons[i][0] <= fatigue:

                # 1. 던전 방문
                visited[i] = True

                # 2. 남은 피로도로 다음 던전 탐색
                dfs(fatigue - dungeons[i][1], count + 1)

                # 3. 방문 기록 복구
                visited[i] = False

    dfs(k, 0)

    return answer