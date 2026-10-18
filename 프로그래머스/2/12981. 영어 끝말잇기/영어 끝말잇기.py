#중복되면 짐 -> set 사용
#앞 단어의 끝말과 연결되면 set검사 -> 없으면 통과
def solution(n, words):

    temp = set()
    temp.add(words[0])
    player, turn = 0,0

    for i in range(1,len(words)):
        if words[i] not in temp:
            if words[i-1][-1] == words[i][0]:
                temp.add(words[i])
            else:
                player = i % n +1
                turn = i //n +1
                return [player, turn]
        else:
            player = i % n +1
            turn = i //n +1
            return [player, turn]
    
    return [player, turn]