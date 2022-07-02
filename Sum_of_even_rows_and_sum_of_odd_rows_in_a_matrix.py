x,y=map(int,input().split())
s=0
c=0
for i in range(x):
    if i%2==0:
        I=list(map(int,input().split()))
        s+=sum(I)
    else:
        I=list(map(int,input().split()))
        c+=sum(I)
print(s,end=" ")
print(c)