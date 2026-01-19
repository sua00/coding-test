def solution(my_string, overwrite_string, s):
    answer = ''
    add_ = len(overwrite_string)
    
    if s+len(overwrite_string) < len(my_string):
        answer = my_string[0:s] + overwrite_string + my_string[s+add_:]
    else : 
        answer = my_string[0:s] + overwrite_string
    return answer