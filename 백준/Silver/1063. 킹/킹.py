king = ''
stone = ''
nums = 0
input_ =[]
moves = []

input_ = input().split(" ")
king = input_[0]
stone = input_[1]
nums = int(input_[2])

for i in range(nums):
    moves.append(input())
    
def str_to_pos(pos):
    return [ord(pos[0]) - 64, int(pos[1])]

def pos_to_str(pos):
    return chr(pos[0] + 64) + str(pos[1])

def moving(move, position):
    x, y = position

    if move == 'R':
        x += 1
    elif move == 'L':
        x -= 1
    elif move == 'B':
        y -= 1
    elif move == 'T':
        y += 1
    elif move == 'RT':
        x += 1
        y += 1
    elif move == 'LT':
        x -= 1
        y += 1
    elif move == 'RB':
        x += 1
        y -= 1
    elif move == 'LB':
        x -= 1
        y -= 1

    return [x, y]

king_pos = str_to_pos(king)
stone_pos = str_to_pos(stone)

for move in moves:

    king_move = moving(move, king_pos)

    if not (1 <= king_move[0] <= 8 and 1 <= king_move[1] <= 8):
        continue

    if king_move == stone_pos:
        stone_move = moving(move, stone_pos)
        
        if not (1 <= stone_move[0] <= 8 and 1 <= stone_move[1] <= 8):
            continue

        stone_pos = stone_move

    king_pos = king_move


print(pos_to_str(king_pos))
print(pos_to_str(stone_pos))