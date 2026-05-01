h,m,s=map(int,input().split())
x=s//60
s=s%60
m=m+x
x=m//60
m=m%60
h=h+x
h=h%24
if h//10==0:
    print('0{}:'.format(h),end='')
else:
    print("{}:".format(h),end='')
if m//10==0:  
    print('0{}:'.format(m),end='')
else:
    print('{}:'.format(m),end='')
if s//10==0:  
    print('0{}'.format(s),end='')
else:
    print('{}'.format(s),end='')  
