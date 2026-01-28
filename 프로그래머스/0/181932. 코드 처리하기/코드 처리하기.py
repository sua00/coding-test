def solution(code):
    ret = ''
    code_list = list(code)
    mode = 0
    for i in range(len(code_list)):
        if code_list[i] == '1':
            mode = 1-mode
        else :
            if mode == 0 and i%2 == 0:
                ret += code_list[i]
            elif mode == 1 and i%2 == 1:
                ret += code_list[i]
    if ret == "":
        ret = "EMPTY"
        return ret
    else:
        return ret