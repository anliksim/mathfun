from random import uniform
import math

a = 0
b = 8


def f(x):
    """
    x^3
    """
    return math.pow(x, 1 / 3)


def pythagoras(y, z):
    return math.sqrt(math.pow(y, 2) + math.pow(z, 2))


def is_distance_to_x_axis_smaller_than_equals_f_of_x(x, y, z):
    return pythagoras(y, z) <= f(x)


def is_in_range(x):
    return a <= x <= b


def is_within(x, y, z):
    """
    x liegt zwischen a und b
    AND
    Abstand von der x-Achse <= f(x)
    => sqrt(y^2 + z^2) <= f(x)
    
    :param x: 
    :param y: 
    :param z: 
    :return:  
    """
    return is_in_range(x) and is_distance_to_x_axis_smaller_than_equals_f_of_x(x, y, z)


def volume(n):
    # Punkte im Koerper
    n_in = 0
    for i in range(n):
        x = uniform(0, 8)
        y = uniform(-2, 2)
        z = uniform(-2, 2)

        if is_within(x, y, z):
            n_in += 1

    vol_quader = 8 * 4 * 4
    return (n_in / n) * vol_quader


print(volume(10000))