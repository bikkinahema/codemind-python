n=input()
w=n.split()
s='a','e','i','o','u'
c=0
for i in w:
    l=len(i)
    for j in i:
        if j in s:
            if i[l-1] not in s:
                c+=1
        l-=1
print(c)

