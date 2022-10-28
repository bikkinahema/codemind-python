n=input()
v='a','e','i','o','u','A','E','I','O','U'
c=0
s=' '
for i in n:
    if i in s:
        continue
    if i in v:
        c+=1
        s+=i
        print(i,end=' ')
if c==0:
    print("-1")
