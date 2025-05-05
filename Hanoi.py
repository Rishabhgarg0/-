def hanoi(n,a,b,c):
    if (n==1):
        print("Move the disc from",a,"to disc",b)
        return
    
    hanoi(n-1,a,c,b)
    print("Move disc",n,"from rod",a,"to rod",b)
    hanoi(n-1,c,b,a)
    
n = 3

hanoi(n,"A","C","B")
