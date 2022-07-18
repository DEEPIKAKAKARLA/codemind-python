testCase=int(input())
for _ in range(testCase):
    n,k=map(int,input().split())
    I=list(map(int,input().split()))
    x=k%n
    print(*(I[n-x:]+I[:n-x]))