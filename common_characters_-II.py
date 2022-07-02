x=input().lower()
y=input().lower()
I=[]
c=0
for i in x:
    if i in y:
        I.append(i)
for j in sorted(set(I)):
    if j!=' ':
        c+=1
print(c)