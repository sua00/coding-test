height = int(input())
tree = []
for i in range(height):
    tree.append(list(map(int, input().split())))

for i in range(height-1,0,-1):
    leaf = tree[i]
    target = tree[i-1]
    for j in range(len(target)):
        target[j] += max(leaf[j],leaf[j+1])
print(tree[0][0])