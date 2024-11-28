#長さ N の重複した要素の無い数列 A と整数 K が与えられるので、
#A に K が含まれていれば "YES" を、そうでなければ "NO" を出力してください。

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

found=False
for a in A:
    if a == K:
        found=True
        break

if found == True:
    print("YES")
else:
    print("NO")