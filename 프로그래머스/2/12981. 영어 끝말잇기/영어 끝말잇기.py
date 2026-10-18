def solution(n, words):
    answer = []
    player, turn =0,0

    #words 순서대로 참가자들이 말함
    #앞선 단어와 뒤의 단어의 첫번째 알파벳이 다르면 -> 탈락
    #같은 단어를 이야기해도 -> 탈락
    #모두 아니면 [0,0]
    
    visited = set()
    visited.add(words[0])
    
    for i in range(1, len(words)):
        if words[i] in visited:
            player = i % n +1
            turn = i//n +1
            return [player, turn]
        
        if words[i-1][-1] != words[i][0]:
            player = i % n +1
            turn = i//n +1
            return [player, turn]
        
        visited.add(words[i])
    
    return[0,0]
        