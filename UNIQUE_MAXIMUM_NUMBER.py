n=int(input())
a=list(map(int,input().split()))
c=0
I=[]
for i in range(n):
    for j in range(n):
        if(a[i]==a[j]):
            c+=1
    if c==1:
        I.append(a[i])
    c=0
if len(I)==0:
    print('-1')
elif I!=0:
    print(max(I))