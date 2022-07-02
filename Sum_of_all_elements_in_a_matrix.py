x,y=map(int,input().split())
s=0
for i in range(x):
    I=list(map(int,input().split()))
    s+=sum(I)
print(s)