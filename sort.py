
def sort(N):
    #a = [5,3,7,10,1,2,4]
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if(j >= 1):
                if(a[j-1] > a[j]):
                    tmp = a[j-1]
                    a[j-1] = a[j]
                    a[j] = tmp
    print(a)

a = [5,3,7,10,1,2,4]
sort(a)