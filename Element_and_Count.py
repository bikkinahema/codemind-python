n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i in a:
        continue
    else:
        k=l.count(i)
        a.append(i)
        print(i,k,end=" ")

        