n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if a[i]%2==0:
        min=0
        if min<i:
            min=a[i]
            c+=1
if c==0:
    print('10')
else:
    print(min)