n=int(input())
count=0
while(n>0):
    r=n%10
    n=n//10
    count+=1
if(count==10 and r!=0):
    print("Valid")
else:
    print("Invalid")