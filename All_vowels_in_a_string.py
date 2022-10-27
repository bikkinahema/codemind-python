n=input()
c=0
d=0
e=0
f=0
k=0
p=0
q=0
r=0
s=0
t=0
for i in n:
    if i=='a':
        c+=1
    if i=='e':
        d+=1
    if i=='i':
        e+=1
    if i=='o':
        f+=1
    if i=='u':
        k+=1
    if i=='A':
        p+=1
    if i=='E':
        q+=1
    if i=='I':
        r+=1
    if i=='O':
        s+=1
    if i=='U':
        t+=1
if (c>=1 and d>=1 and e>=1 and f>=1 and k>=1) or (p>=1 and q>=1 and r>=1 and s>=1 and t>=1):
    print("True")
else:
    print("False")
    