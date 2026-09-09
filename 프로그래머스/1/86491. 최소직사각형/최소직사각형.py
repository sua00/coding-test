def solution(sizes):
    answer = 0
    max_w, max_h=0,0
    for size in sizes:
        temp = 0
        w, h = size
        if w < h :
            temp = h
            h = w
            w= temp
        if max_w < w:
            max_w = w
        if max_h < h:
            max_h = h
    answer = max_h * max_w
    
    return answer