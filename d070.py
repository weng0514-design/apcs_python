#d070. 格瑞哥里的煩惱 (0 尾版)
while True:
    y=int(input())
    if y==0:
        break
    if y%400==0 or y%4==0 and y%100!=0:
        print("a leap year")
    else:
        print("a normal year")
