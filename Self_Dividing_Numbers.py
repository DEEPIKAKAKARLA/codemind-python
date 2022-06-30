n=int(input())
m=int(input())
for i in range(n,m+1):
    t,c,s=i,0,0
    while(t!=0):
        d=t%10
        t=t//10
        c+=1
        if(d==0):
            break
        if(i%d==0):
            s+=1
    if(s==c):
        print(i,end=' ')