#d067. 格瑞哥里的煩惱 (1 行版)
a=int(input())
if a%400==0 or (a%4==0 and a%100!=0):
    print("a leap year")
else:
    print("a normal year")
