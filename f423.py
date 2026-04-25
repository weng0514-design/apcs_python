r=0
n=int(input())
if n%2==0:
  n=n-1
for i in range(1,n+1,2):
  r=r+i
print(r)
