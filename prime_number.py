N=int(input())
count=0
for i in range(1,N+1,1):
    if(N%i==0):
        count+=1
if(count==2):
    print('prime')
else:
    print('not a prime')