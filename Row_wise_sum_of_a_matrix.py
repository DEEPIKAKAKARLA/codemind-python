x,y=map(int,input().split())
c=[]
d=[]
for i in range(x):
    I=list(map(int,input().split()))
    d.append(sum(I))
print(*d)