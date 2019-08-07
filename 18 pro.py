have,sor=map(int,input().split())
don=[]
gon=0
for i in range(have):
    don.append(list(map(int,input().split())))   
for i in range(have):
    for j in range(sor-1):
        for k in range(j+1,sor+1):
            if don[i][j:k]==[1]*len(don[i][j:k]):
                 if all(don[p+i][j:k]==[1]*len(don[p+i][j:k]) for p in range(len(don[i][j:k])-1)):
                     if len(don[i][j:k])>gon:
                        gon=len(don[i][j:k])
if len(don)==1 and len(don[0])==1 and don[0][0]==1:
    print(1)
for i in range(gon):
    print(*[1]*gon)
