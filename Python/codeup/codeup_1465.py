n,m=list(map(int,input().split()))
nm_list=[]
start=0
for i in range(n):
    nm_list.append([])
    for j in range(m):
        start+=1
        nm_list[i].append(start)
for i in range(n-1,-1,-1):
    for j in range(m):
        print(nm_list[i][j],end=" ")
    print()