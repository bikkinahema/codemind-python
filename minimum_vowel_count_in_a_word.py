n=input()
w=n.split()
v='a','e','i','o','u'
m=5
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
print(m)
        