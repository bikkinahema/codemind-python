n=input()
n=n.replace(" ","")
n=n.lower()
s=''
for i in n:
    if i in s:
        continue
    else:
        s+=i
l=[]
for i in s:
    p=ord(i)
    l.append(p)
f=sorted(l)
for i in f:
    o=chr(i)
    print(o,end='')