n=int(input())
square=pow(n,2)
mod=pow(10,len(str(n)))
if square%mod==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")