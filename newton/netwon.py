import math
import argparse
import matplotlib.pyplot as plt

X = []
d = 1


def f(x):
    return math.pow(x, 2) - 2 * math.cos(x)
    # return x * math.pow(math.e, -x)
    # return math.pow(x,3) + 5*x - 4


def f1(x):
    return 2 * x + 2 * math.sin(x)
    # return (1 - x) * math.pow(math.e, -x)
    # return 3*math.pow(x,2) + 5


def newton(x0):
    X.append(x0)
    x1 = x0 - f(x0) / f1(x0)
    if x0 != x1:
        print(x1)
        return newton(x1)


def plot():
    y = []
    for x in X:
        y.append(f(x))

    plt.plot(X, y, 'ro')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fucking awesome!')
    parser.add_argument('-x', '--x', type=float, required=False, default=d)
    args = parser.parse_args()
    newton(args.x)
    # plot()
