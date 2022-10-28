n=input()
v='a','e','i','o','u'
s=' '
for i in n:
    if i in s:
        continue
    if i in v:
        s+=i
c=0
for i in v:
    if i not in s:
        print(i,end=' ')
    if i in s:
        c+=1
if c==5:
    print("0")
