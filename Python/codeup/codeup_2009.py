a,b=list(map(int,input().split()))
dap=0
while int(a/b)!=0:
    dap+=int(a/b)
    a=a-int(a/b)*b+int(a/b)
print(dap)