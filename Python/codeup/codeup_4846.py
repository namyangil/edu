n=int(input())
hap=0
for i in range(n):
    a,b=list(map(int,input().split()))
    hap+=b%a
print(hap)