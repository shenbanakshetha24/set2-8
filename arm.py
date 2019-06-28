a,b=map(int,input().split())
for n in range(a,b+1):
 order=len(str(num))
 s=0
 t=n
 while t>0:
  digit =t%10
  s +=digit ** 3
  t //=10
 if n==s:
  print(n,end=" ")
