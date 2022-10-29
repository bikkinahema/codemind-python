s1=input()
s2=input()
w1=s1.split()
w2=s2.split()
k=[]
l=[]
for i in w1:
    if i in w2:
        k.append(i)
for i in k:
    if w1.count(i)==1:
        if w2.count(i)==1:
            l.append(i)
print(len(l))