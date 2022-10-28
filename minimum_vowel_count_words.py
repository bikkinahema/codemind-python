n=input()
w=n.split()
v='a','e','i','o','u'
m=5
d=0
for i in w:
    c=0
    for j in i:
        s=' '
        if j in s:
            continue
        if j in v:
            c+=1
    if c<=m:
        m=c
for i in w:
    l=0
    for j in i:
        p=''
        if j in s:
            continue
        if j in v:
            l+=1
    if l==m:
        d+=1
print(d)