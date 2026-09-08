from collections import deque

def solution(game_board, table):
    
    def normalize(shape):
        min_x = min(x for x, y in shape)
        min_y = min(y for x, y in shape)

        new_shape = []

        for x, y in shape:
            new_shape.append((x - min_x, y - min_y))

        new_shape.sort()

        return new_shape


    def rotate(shape):
        rotated = []

        for x, y in shape:
            rotated.append((y, -x))

        return normalize(rotated)


    def get_blank_shapes(game_board):
        n = len(game_board)
        visited = [[False] * n for _ in range(n)]
        blanks = []

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(n):
            for j in range(n):

                if game_board[i][j] == 0 and not visited[i][j]:

                    queue = deque()
                    queue.append((i, j))
                    visited[i][j] = True

                    shape = []

                    while queue:
                        x, y = queue.popleft()
                        shape.append((x, y))

                        for d in range(4):
                            nx = x + dx[d]
                            ny = y + dy[d]

                            if 0 <= nx < n and 0 <= ny < n:
                                if game_board[nx][ny] == 0 and not visited[nx][ny]:
                                    visited[nx][ny] = True
                                    queue.append((nx, ny))

                    blanks.append(normalize(shape))

        return blanks


    def get_piece_shapes(table):
        n = len(table)
        visited = [[False] * n for _ in range(n)]
        pieces = []

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(n):
            for j in range(n):

                if table[i][j] == 1 and not visited[i][j]:

                    queue = deque()
                    queue.append((i, j))
                    visited[i][j] = True

                    shape = []

                    while queue:
                        x, y = queue.popleft()
                        shape.append((x, y))

                        for d in range(4):
                            nx = x + dx[d]
                            ny = y + dy[d]

                            if 0 <= nx < n and 0 <= ny < n:
                                if table[nx][ny] == 1 and not visited[nx][ny]:
                                    visited[nx][ny] = True
                                    queue.append((nx, ny))

                    pieces.append(normalize(shape))

        return pieces


    blanks = get_blank_shapes(game_board)
    pieces = get_piece_shapes(table)

    used = [False] * len(pieces)

    answer = 0

    for blank in blanks:

        for i in range(len(pieces)):

            if used[i]:
                continue

            # 칸 개수가 다르면 모양 비교할 필요 없음
            if len(blank) != len(pieces[i]):
                continue

            piece = pieces[i]

            # 0도, 90도, 180도, 270도 확인
            for _ in range(4):

                if blank == piece:
                    used[i] = True
                    answer += len(blank)
                    break

                piece = rotate(piece)

            # 현재 빈칸에 퍼즐을 넣었으면 다음 빈칸으로
            if used[i]:
                break

    return answer