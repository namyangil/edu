a,b=list(map(int,input().split()))
for i in range(a,b+1):
    flag=""
    str_i=str(i)
    for j in range(len(str_i)):
        if str_i[j]=="3" or str_i[j]=="6" or str_i[j]=="9":
            flag+="K"
    if flag=="":
        print(i)
    else:
        print(flag)