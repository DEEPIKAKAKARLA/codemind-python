x,y=map(int,input().split())
s=0
for i in range(x):
    n=list(map(int,input().split()))
    for j in range(len(n)):
        if j==i or j==len(n)-1-i:
            s+=n[j]
print(s)