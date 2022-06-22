n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    if a[i]%2!=0:
        max=0
        if max<i:
            max=a[i]
print(max)