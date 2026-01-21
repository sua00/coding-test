str_ = input()
counts = [0]*26

str_ = str.lower(str_)
for char_ in str_:
    index = ord(char_)-97
    counts[index] += 1

if counts.count(max(counts)) >= 2:
    print('?')
else :
    print(chr(counts.index(max(counts))+65))