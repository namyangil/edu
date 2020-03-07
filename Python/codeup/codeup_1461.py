n=int(input())
n_list=[]
start=0
for i in range(n):
    n_list.append([])
    for j in range(n):
        start+=1
        n_list[i].append(start)
for i in range(n):
    for j in range(n-1,-1,-1):
        print(n_list[i][j],end=" ")
    print()