b186. 97七區資訊學科1(改編)
while True:
    try:
       a,b,c=map(int,input().split())
       if a//10>c//2:
           k=c//2
       else:
           k=a//10
       print("{} 個餅乾，{} 盒巧克力，{} 個蛋糕。 ".format(a,b+k,c))
    except:
        break
