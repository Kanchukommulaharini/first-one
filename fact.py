def fact(n)
f=1
for i in range(1,n+1)
f=f*i
return f
def febanocci(n)
s=list()
a=0
b=1
while a<n
  c=a+b
  s.append(a)
a=b
b=c
return s

