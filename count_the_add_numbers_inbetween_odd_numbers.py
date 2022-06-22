n=int(input())
s=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    if s[i-1]%2!=0 and s[i]%2!=0 and s[i+1]%2!=0:
        c+=1
print(c)