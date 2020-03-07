n=int(input())
n_list=list(map(int,input().split()))
new_list=sorted(n_list,reverse=True)
for i in n_list:
    for j in range(n):
        if i==new_list[j]:
            print(j+1)
            break