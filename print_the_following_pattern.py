n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            j=''
            print(j,end='0')
        else:
            print('x',end='')
    print()