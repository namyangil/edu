n,m=list(map(int,input().split()))
nm_list=[]
start_x=n*m-n+1
for i in range(n):
    nm_list.append([])
    start_y=start_x
    for j in range(m):
        nm_list[i].append(start_y)
        start_y-=n
    start_x+=1
for i in range(n):
    for j in range(m):
        print(nm_list[i][j],end=" ")
    print()