n=int(input())
n_list=list(map(int,input().split()))
n_max=max(n_list)
n_min=min(n_list)
for i in range(n):
    if n_max==n_list[i]:
        print("{} : {}".format(i+1,n_max))
        break
for j in range(n):
    if n_min==n_list[j]:
        print("{} : {}".format(j+1,n_min))
        break