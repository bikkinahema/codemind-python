n=input()
s=n.split()
for i in s:
    min=ord(i[0])
    for j in range(1,len(i)):
        if ord(i[j])<min:
            min=ord(i[j])
    x=chr(min)
    print(x,end=' ')
    break
for k in s[::-1]:
    max=ord(k[0])
    for l in range(1,len(k),1):
        if ord(k[l])>max:
            max=ord(k[l])
    y=chr(max)
    print(y)
    break