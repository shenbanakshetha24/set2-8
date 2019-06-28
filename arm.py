c,d=map(int,input().split())
for n in range(c,d+1):
 order=len(str(n))
 s=0
 t=n
 while t>0:
  digit =t%10
  s +=digit ** 3
  t //=10
 if n==s:
  print(n,end=" ")
