# Week-8 Quiz Assignment Answer
# 1.A,B,C
# 2.A,B,c
# 3.C
# 4.A
# 5.A
# 6.B
# 7.B
# 8.C
# 9.B
# 10.1


def subStr(s1, s2):
    M = len(s1)
    N = len(s2)

    for i in range(M - N + 1):
        flag = True
        for j in range(N):
            if (s1[i + j] != s2[j]):
                flag = False
                break

        if flag :
            return True
    return False

if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(subStr(s1, s2),end="")