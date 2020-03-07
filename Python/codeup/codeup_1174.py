a,b=list(map(int,input().split()))
temp=a*60+b
temp-=30
temp=24*60+temp
temp=int(temp%(24*60))
hour=int(temp/60)
minute=temp%60
print("{} {}".format(hour,minute))