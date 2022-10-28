n=input()
n=n.replace(" ","")
n=n.lower()
l=[]
c=0
for i in n:
    l.append(i)
for i in l:
    if l.count(i)==1:
        c+=1
        print(i)
        break
if c==0:
    print("-1")
    