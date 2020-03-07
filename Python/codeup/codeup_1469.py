n=int(input())
n_list=[]
start=0
for i in range(n):
    n_list.append([])
    for j in range(n):
        start+=1
        n_list[i].append(start)
start=n
for i in range(n):
    if start==n:
        for j in range(n):
            start-=1
            print(n_list[i][start],end=" ")
    elif start==0:
        for j in range(n):
            print(n_list[i][start],end=" ")
            start+=1
    print()