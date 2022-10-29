s1=input()
s2=input()
s1=s1.replace(" ","")
s2=s2.replace(" ","")
s1=s1.lower()
s2=s2.lower()
l=[]
for i in s1:
    if i in l:
        continue
    if i in s2:
        l.append(i)
f=sorted(l)
for i in f:
    print(i,end='')
if len(l)==0:
    print("-1")