N=int(input())
ans=0
rev=0
sqcount=0
revsqcount=0
sq=pow(N,2)
sq1=sq
while(sq1>0):
    sqcount+=1
    sq1=sq1//10
x=N
while(x>0):
    r=x%10
    rev=(rev*10)+r
    x=x//10
revsq=pow(rev,2)
revsq1=revsq
while(revsq1>0):
    revsqcount+=1
    revsq1=revsq1//10
while(sq>0):
    t=sq%10
    ans=(ans*10)+t
    sq=sq//10
if(ans==revsq and sqcount==revsqcount):
    print("True")
else:
    print("False")