def fibo(N):
    a = [i for i in range(0, N)]
    if (N <= 30):
        for i in range(1, N):
            if (i >= 3):
                a[i] = a[i-1]+a[i-2]
    print(a)         

fibo(20)
          
    
