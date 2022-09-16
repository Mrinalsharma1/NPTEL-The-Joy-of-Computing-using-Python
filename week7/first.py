# Week-7 Quiz Assignment Answer
# 1.C
# 2.A
# 3.A,B,C
# 4.A,C
# 5.B
# 6.B
# 7.B
# 8.D
# 9.C
# 10.B

    
def DiagCalc(M):
  sum1=0
  sum2=0
  for i in range(n):
    sum1+=M[i][i]
    sum2+=M[i][n-i-1]        
  print(sum1)
  print(sum2,end="")                
