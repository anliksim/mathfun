b = 0.25
m = 0.05
p = 0.01


def calc2(y):
    return (0.2 - 0.15) * y


def calc3(y):
    return (b - m - p * y) * y


def simulate(y, t, s, calc):
    n = int(t / s)
    for i in range(n):
        y = y + s * calc(y)

    return y


def simulate2(y, t, s):
    return simulate(y, t, s, calc2)


def simulate3(y, t, s):
    return simulate(y, t, s, calc3)


assert 11025.0 == simulate2(10000, 2, 1)

# A2c
# print(simulate2(2, 3, 0.5))

# A2d
# print(simulate2(100, 6, 0.01))

# A3
# print(simulate3(10, 2, 0.5))
print(simulate3(12.5, 8, 0.5))
