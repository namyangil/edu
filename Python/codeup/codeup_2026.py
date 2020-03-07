n=int(input(),16)
re_n=str(format(n,"b"))
while len(re_n)%4!=0:
    re_n="0"+re_n
for i in range(len(re_n)):
    print(re_n[i],end="")
    if i%4==3:
        print(" ",end="")