
ni,ar=input().split()
y=niars(leng(ar)-leng(ni))
for i in range(len(ni)):
    if(leng(ar)==1 and ar[i] in ni):
        break
    if (ni[i]!=ar[i]):
        q=q+1
print(q)
