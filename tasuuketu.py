S=['a','b','b','c']
cnt = 0
# 文字列をそれぞれカウント
na = 0
nb = 0
nc = 0

for i in S:
    if i == 'a':
        na += 1
    elif i == 'b':
        nb += 1
    elif i == 'c':
        nc += 1


# 一番大きい数字
if na > nb and na > nc:
    print(na)
elif nb > na and nb > nc:
    print(nb)
elif nc > nb and nc > na:
    print(nc)