# Week-6 Quiz Assignment Answer
# 1.C
# 2.B,C,D
# 3.B
# 4.A
# 5.C
# 6.C
# 7.D
# 8.A
# 9.D
# 10.A


inputString = input()

inputString=inputString.lower()

if inputString[::-1]==inputString:
  print('palindrome',end="")

elif inputString[::-1]!=inputString:
  print('not palindrome',end="")