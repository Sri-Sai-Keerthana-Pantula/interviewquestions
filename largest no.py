a=[1,2,8,9,4]
'''
max(a)
'''
m=a[0]
i=0
for i in range(len(a)):
    #for j in range(1,len(a)):
        #print(m,a[j])
        if m<a[i]:
         #   print("hi")
            m=a[i]
print(m)
