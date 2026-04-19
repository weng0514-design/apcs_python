d984. 棄保效應
while True:
    try:
        a=list(map(int,input().split()))
        b=sorted(a,reverse=True)#由大到小
        if b[0]>b[1]+b[2]:
            win=b[0]
        else:
            win=b[1]
        k=a.index(win)#找到a串列的索引值為何
        if k==0:
            print("A")
        elif k==1:
            print("B")
        else:
            print("C")    
    except:
        break
