n=int(input())
a=list(map(int,input().split()))
I=[]
for i in range(n):
    if a[i]%2==0:
        I.append(i)
print(max(I))