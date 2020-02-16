import random as rd
def cal(t):
    return 2/((abs(t-7)+7)/7+1)
def rand():
    return 1+0.04*rd.randint(-2,2)

print(rand())