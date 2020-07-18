a="hi hello"
for i in range(len(a)):
    if a[i]==" ":
        print("i",i)
        a=a[0:i]+a[(i+1):]
        print(a)
        break

'''
string = string.replace(' ','')
'''
