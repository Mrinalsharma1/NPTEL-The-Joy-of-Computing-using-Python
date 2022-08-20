S=input()
v=list('aeiou')
a=""
for i in S:
  if  i.lower() in v:
    a=a+'*'
  else:
    a=a+i
print(a,end="")