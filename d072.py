d072. 格瑞哥里的煩惱 (Case 版)
t=int(input())
for i in range(t):
    a=int(input())
    if a%400==0 or (a%4==0 and a%100!=0):
        print("Case {}: a leap year".format(i+1))
    else:
        print("Case {}: a normal year".format(i+1))
