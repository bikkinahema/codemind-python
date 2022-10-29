s1=input()
s2=input()
s1=s1.replace(" ","")
s2=s2.replace(" ","")
s1=s1.lower()
s2=s2.lower()
l=[]
k=[]
for i in s1:
    if i in l:
        continue
    if i not in s2:
        k.append(i)
    l.append(i)
p=[]
for i in s2:
    if i in p:
        continue
    if i not in s1:
        k.append(i)
    p.append(i)
f=sorted(k)
for i in f:
    print(i,end='')
        