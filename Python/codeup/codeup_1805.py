n=int(input())
n_list=[]
new_list=[]
temp=""
for i in range(n):
    n_list.append(input().split())
new_list=sorted(n_list, key=lambda n:int(n[0]))  # 리스트 기준을 정해서 정렬하기
for i in new_list:
    temp=" ".join(i)  # 리스트에서 문자열을 [] 없이 출력하기
    print(temp)