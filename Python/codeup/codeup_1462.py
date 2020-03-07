n=int(input())
n_list=[]
start=0
for i in range(n):
    n_list.append([])
    for j in range(n):
        start+=1
        n_list[i].append(start)
for i in range(n):
    for j in range(n):
        print(n_list[j][i],end=" ")
    print()