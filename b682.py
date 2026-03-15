#b682. 2. 同學早安
h1,m1=map(int,input().split())
h2,m2=map(int,input().split())    
t1=h1*60+m1  
t2=h2*60+m2
t=t2-t1    
if t<0:
    t+=24*60    
print(t//60,t%60)
