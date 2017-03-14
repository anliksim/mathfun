from statistics import mean
import matplotlib.pyplot as plt

# x = [1, 4, 5, 8, 9]
# y = [6, 12, 14, 18, 19]

x = [10, 42, 38, 15, 22, 32, 40, 14, 26, 32, 38, 25, 48, 28, 22, 45, 18, 24, 30, 43]
y = [450, 1050, 900, 525, 710, 854, 800, 493, 730, 894, 940, 733, 985, 763, 583, 850, 798, 754, 805, 1085]

def calc_a(x, y, xBar, yBar):
    summ = 0
    divider = 0
    for index, ele in enumerate(x):
        summ += (ele - xBar) * (y[index] - yBar)
        divider += pow((ele - xBar), 2)
    return summ / divider


def calc_b(a, xBar, yBar):
    return yBar - a * xBar


def calc_y(a, x, b):
    new_y = []
    for p in x:
        new_y.append(a*p + b)
    return  new_y


def line_fit(x,y):
    x_bar = mean(x)
    y_bar = mean(y)
    a = calc_a(x, y, x_bar, y_bar)
    b = calc_b(a, x_bar, y_bar)
    return (a, b)


a, b = line_fit(x,y)
print(a, b)

plt.plot(x, y, 'ro')
plt.xlabel('Anbieter A')
plt.ylabel('Anbieter B')
plt.plot(x, calc_y(a, x, b)) # Aufgabe 2 (Gerade)
plt.show()