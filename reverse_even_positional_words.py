s=input()
w=s.split()
for i in range(0,len(w)):
    k=' '
    if i%2==0:
        k=w[i]
        p=k[::-1]
        print(p,end= ' ')
    else:
        print(w[i],end=' ')
        