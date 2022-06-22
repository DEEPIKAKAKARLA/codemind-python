n=int(input())
a=list(map(int,input().split()))
s=int(input())
c=0
for i in range(n):
    if s==a[i]:
        c+=1
print(c)