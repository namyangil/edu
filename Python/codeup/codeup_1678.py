n_list=[]
temp=0
total=0
for i in range(5):
    n_list.append(list(map(int,input().split())))
for i in range(3):
    for j in range(3):
        temp=sum(n_list[i][j:j+3])+sum(n_list[i+1][j:j+3])+sum(n_list[i+2][j:j+3])
        if temp>total:
            total=temp
print(total)