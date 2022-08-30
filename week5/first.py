from re import A


# // Quiz Question Answer
# 1.D
# 2.D
# 3.A
# 4.B
# 5.A
# 6.D
# 7.A,D
# 8.B
# 9.A
# 10.B

def count_letters(S):
    d={}
    for i in S:
        d[i]=0
    for i in S:
        d[i]+=1
        
    return d