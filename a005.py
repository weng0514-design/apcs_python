a005. Eva 的回家作業   
x=int(input())
for i in range(x):
    a= list(map(int, input().split()))
    if a[1]-a[0]==a[2]-a[1]:
        d=a[1]-a[0]
        a.append(a[3]+d)
    else:
        d=a[1]/a[0]
        a.append(int(a[3]*d))
    for k in a:
        print("{}".format(k),end=" ")
    
    print()
    
