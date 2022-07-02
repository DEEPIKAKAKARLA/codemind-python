x,y=map(int,input().split())
s=0
c=0
for i in range(x):
    I=list(map(int,input().split()))
    for j in I:
        if j%2==1:
            s+=j
        else:
            c+=j
print(c,end=" ")
print(s)