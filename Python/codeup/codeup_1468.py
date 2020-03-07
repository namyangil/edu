n=int(input())
n_list=[]
start=0
for i in range(n):
    n_list.append([])
    for j in range(n):
        start+=1
        n_list[i].append(start)
start=0
for i in range(n):
    if start==0:
        for j in range(n):
            print(n_list[i][start],end=" ")
            start+=1
    elif start==n:
        for j in range(n):
            start-=1
            print(n_list[i][start],end=" ")
    print()