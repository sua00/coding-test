def solution(sizes):
    answer_h = 0
    answer_w = 0
    #가로, 세로 중 더 긴 값을 가로로 통일
    for size in sizes:
        width, height = size[0], size[1]
        if width < height:
            size[0] = height
            size[1] = width
        
    for size in sizes:
        width, height = size[0], size[1]
        if width > answer_w:
            answer_w = width
        if height > answer_h:
            answer_h = height
        
    answer = answer_w * answer_h
    return answer