n=int(input())
n_list=[]
temp=""
for i in range(n):
    n_list.append([input()])
for i in n_list:
    temp="".join(i)   #리스트를 문자열로 저장하기
    for j in range(len(temp)-1,-1,-1):
        print(temp[j],end="")    
    print()