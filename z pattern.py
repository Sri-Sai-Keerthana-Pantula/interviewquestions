'''
a=1
b=4
for i in range(0,6):
    for j in range(6):
        #print("i",i)
        #print("j",j)
        #print("4-i",4-i)
        if i==0 or i==5:
            print("*",end='')
        elif i==a and j==b:
            print("*",end='')
            a=a+1
            b=b-1
        else:
            print(" ",end='')
    print()
'''
for i in range(5):
    for j in range(5):
        #print("i",i)
        #print("j",j)
        #print("4-i",4-i)
        if i==0 or i==4:
            print("*",end='')
        elif j==4-i:
            print("*",end='')
        else:
            print(" ",end='')
    print()
       
