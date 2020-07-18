n=1
i=0
s=0
a=n
while(n>0):
    r=n%10
    n=int(n/10)
    #print("r,n",r,n)
    s=r**3+s
    #print(s)
if s==a:
    print("amstrong")
else:
    print("not amstrong")
    
    
