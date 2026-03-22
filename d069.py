#d069. 格瑞哥里的煩惱 (t 行版)
t=int(input())
for i in range(t):
    a=int(input())
    if a%400==0 or (a%4==0 and a%100!=0):
        print("a leap year")
    else:
        print("a normal year")
