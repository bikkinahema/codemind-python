n1,n2=map(int,input().split())
p=str(n1)
t=p[0:n2]
k=p[-n2:]
t=int(t)
k=int(k)
print(abs(k-t))
