n_list=list(map(int,input().split()))
ave=sum(n_list)/len(n_list)
up=0
down=0
print("{:0.1f}".format(ave))
for i in range(len(n_list)):
    if n_list[i]>=ave:
        up+=1
    else:
        down+=1
print(up,down)