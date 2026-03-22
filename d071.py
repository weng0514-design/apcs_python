#d071. 格瑞哥里的煩惱 (EOF 版) -- 板橋高中 教學題
while True:
    try:
        a=int(input())
        if a%400==0 or (a%4==0 and a%100!=0):
            print("a leap year")
        else:
            print("a normal year")
    except:
        break
