n=input()
n=n.replace(" ","")
n=n.lower()
l=[]
c=0
for i in n:
        l.append(i)
f=[]
for i in l:
    if l.count(i)==1:
        f.append(i)
f=sorted(f)
for i in f:
    print(i,end='')