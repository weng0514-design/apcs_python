s=0
a=0
while True:
    n=int(input())
    if n == -1:
       break
    s += n
    a += 1
print("%.1f"%(s/a))
