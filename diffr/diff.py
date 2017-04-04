import math


def func(x, y):
    return 2 * x + y + 1


def calc_h(x0, xn, n):
    return (xn - x0) / n


def calc_x(x, h):
    return x + h


def calc_y(x, y, h):
    return y + h * func(x, y)


def euler_method(xn, n):
    x = 0
    y = 2
    h = calc_h(x, xn, n)
    for i in range(n):
        y = calc_y(x, y, h)
        x = calc_x(x, h)
    return y


def y(x):
    return 5 * math.pow(math.e, x) - 2 * x - 3


x = 3
res_y = y(x)

print("y: ", res_y)

n = 100
while euler_method(x, n) <= res_y - 0.02:
    n += 1000

print("a: ", euler_method(x, n))
print("n: ", n)
