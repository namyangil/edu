n=int(input())
n_list=[]
start=0
for i in range(n):
    n_list.append([])
    for j in range(n):
        start+=1
        n_list[i].append(start)
start_x=0
start_y=n-1
for i in range(n):
    for j in range(n):
        if j%2==1:
            print(n_list[j][start_x],end=" ")
        else:
            start-=1
            print(n_list[j][start_y],end=" ")
    print()
    start_x+=1
    start_y-=1