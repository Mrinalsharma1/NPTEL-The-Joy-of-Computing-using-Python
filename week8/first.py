# Week-8 Quiz Assignment Answer
# 1.B,C
# 2.C
# 3.A,C
# 4.B
# 5.A
# 6.A
# 7.A,C
# 8.A
# 9.C
# 10.C




def cubeT(l):
  res = tuple([pow(i, 3) for i in l])
  return res

L = [int(i) for i in input().split()]
print(cubeT(L),end="")