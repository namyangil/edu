n,m=list(map(int,input().split()))
nm_list=[]
start=0
for i in range(m):
    nm_list.append([])
    for j in range(n):
        start+=1
        nm_list[i].append(start)
start=n
for i in range(n):
    start-=1
    for j in range(m-1,-1,-1):
        if j%2==1:
            print(nm_list[j][i],end=" ")
        else:
            print(nm_list[j][start],end=" ")
    print()