N=int(input())
sum=0
pro=N*N
while(pro>0):
    r=pro%10
    sum+=r
    pro=pro//10
if(sum==N):
    print("Neon Number")
else:
    print("Not Neon Number")