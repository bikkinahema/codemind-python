s=input()
s=s.replace(" ","")
l=[]
c=0
for i in s:
    if i in l:
        c+=1
        continue
    l.append(i)
if c==0:
    print("True")
else:
    print("False")
    