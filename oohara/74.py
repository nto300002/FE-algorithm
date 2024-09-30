def permutation(c,n,l,r):
    if(l == r):
        result = ''.join(c)
        print(result)
    else:
        for i in range(l, r):
            c[i],c[l] = c[l],c[i]
            print('はじめ:',l+1)
            permutation(c,n,l+1,r)
            c[i],c[l] = c[l],c[i]
            print('あと:',l+1)

permutation(['a','b','c','d'], 4, 0, 4)