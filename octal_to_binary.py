n=int(input())
i,d,b=0,0,0
while n:
    d+=(n%10)*pow(8,i)
    n//=10
    i+=1
i=1
while d:
    b+=(d%2)*i
    d//=2
    i*=10
print(b)