def solution(sizes):
    answer = 0
    temp = 0
    max_w =0
    max_h=0
    for size in sizes:
        w, h = size[0], size[1]
        if w < h:
            temp = h
            h = w
            w = temp
            
        if max_w < w:
            max_w = w
        if max_h < h:
            max_h = h
    answer = max_w * max_h
    return answer