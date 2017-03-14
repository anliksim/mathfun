from statistics import mean
import math
import matplotlib.pyplot as plt

#x = [1, 2, 5, 6, 8]
#y = [3, 9, 40, 53, 85]

# masse
#x = [0.025, 0.2, 0.3, 2, 5, 30, 70, 450]
x = [50]
# ruhepuls
#y = [670, 420, 300, 205, 120, 85, 72, 38]
y = [74]

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


def log10(y):
	new_y = []
	for p in y:
		new_y.append(math.log10(p))
	return new_y
	
	
x_log = log10(x)
y_log = log10(y)
	
a, b = line_fit(x_log,y_log)
	
c = a
d = math.pow(10, b)
print(c, d)

plt.plot(x_log, y_log, 'ro')
plt.xlabel('Masse')
plt.ylabel('Ruhepuls')
plt.plot(x_log, calc_y(a, x_log, b)) # Aufgabe 2 (Gerade)
plt.show()