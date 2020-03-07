n_list=list(map(int,input().split()))
serial=0
for i in n_list:
    serial+=pow(i,2)
print(serial%10)