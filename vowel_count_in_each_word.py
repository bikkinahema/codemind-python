n=input()
w=n.split()
for j in w:
    c=0
    for k in j:
        s=' '
        if k not in s:
            if k=='a' or k=='A':
                c+=1
                s+=k
        if k not in s:
            if k=='e' or k=='E':
                c+=1
                s+=k
        if k not in s:
            if k=='i' or k=='I':
                c+=1
                s+=k
        if k not in s:
            if k=='o' or k=='O':
                c+=1
                s+=k
        if k not in s:
            if k=='u' or k=='U':
                c+=1
                s+=k
    print(c,end=' ')
        