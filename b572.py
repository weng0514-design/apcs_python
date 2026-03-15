#b572. 忘了東西的傑克
p=int(input())
for i in range(p):
    a,b,c,d,e=map(int,input().split())
    k=a*60+b
    l=c*60+d
    if l-k>=e:
        print("Yes")
    else:
        print("No")
