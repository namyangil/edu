n_list=[]
max_num=0
for i in range(9):
    n_list.append(int(input()))
max_num=max(n_list)
print(max_num)
for i in range(9):
    if n_list[i]==max_num:
        print(i+1)
        break