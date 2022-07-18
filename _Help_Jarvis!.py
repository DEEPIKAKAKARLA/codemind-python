t=int(input())
for i in range(t):
    I=input()
    li=[]
    for i in I:
        li.append(int(i))
    mi=min(li)
    m=max(li)
    c=0
    arr=[]
    for i in range(mi,m+1):
        arr.append(i)
    if sorted(li)==sorted(arr):
        print('YES')
    else:
        print('NO')