s1=input()
s2=input()
I1=list(s1.lower().split(" "))
I2=list(s2.lower().split(" "))
c=0
for i in I1:
    if i in I2 :
        c+=1
print(c)