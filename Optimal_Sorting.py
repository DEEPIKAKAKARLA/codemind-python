n=int(input())
c=0
for i in range(n):
    a=int(input())
    I=list(map(int,input().split()))
    for j in range(1,a):
        if I[j-1]>I[j]:
            c+=1
    if c==0:
        print(c)
    else:
        ma=max(I)
        mi=min(I)
        print(ma-mi)