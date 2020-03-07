n_list=input()
if int(n_list)<10:
    print(n_list)
else:
    while(len(n_list)>1):
        temp=0
        for i in range(len(n_list)):
            temp+=int(n_list[i])
        n_list=str(temp)
    print(temp)