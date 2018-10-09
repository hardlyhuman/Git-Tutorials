# The objective of this program is to multiply two input numbers


def multiply(*args):
    a = args
    res = 1
    for ele in a:
        res *= ele

    return res

a1=int(input())
a2=int(input())

print(multiply(a1,a2))
