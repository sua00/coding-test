def solution(sizes):
    answer= 0
    for size in sizes:
        width = size[0]
        height = size[1]
        if width < height:
            size[0] = height
            size[1] = width
    max_width = 0
    max_height = 0
    for size in sizes:
        w = size[0]
        h = size[1]
        if w> max_width:
            max_width = w
        if h > max_height:
            max_height = h
        
    answer= max_width * max_height
        
    return answer
        