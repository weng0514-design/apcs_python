
n=0
for a in range(2001,2101):#range(start,end)
    if a%400==0 or (a%4==0 and a%100!=0):
        print("{}".format(a),end=" ")
        n +=1
        if n%5==0:
            print() 
