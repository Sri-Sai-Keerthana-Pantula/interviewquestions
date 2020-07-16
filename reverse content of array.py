a=[2,1]
l=len(a)
'''
a.reverse()

i=1
t=a[1]
a[1]=a[l-2]
a[l-2]=t
print(a)
i=i+1
'''
i=0
while(i<l/2):
    t=a[i]
    a[i]=a[l-1-i]
    a[l-i-1]=t
    print(a)
    i=i+1
    
