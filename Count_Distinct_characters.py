n=input()
n=n.replace(" ","")
n=n.lower()
l=[]
for i in n:
    if i in l:
        continue
    else:
        l.append(i)
print(len(l))
        