"""
Sum and Product
Write a function that takes in two floating-point numbers s and p and returns a tuple of two floating-point numbers (x, y), where x + y = s and x * y = p. Round x and y to three decimal places.

If there are multiple solutions, return the solution with the lesser x (or lesser y, if the x values are equal).

Imaginary/complex number solutions are not allowed. If no real-valued solutions exist, return None.

Examples
sum_and_product(2, -15) ➞ (-3.0, 5.0)

sum_and_product(144, 144) ➞ (1.007, 142.993)

sum_and_product(-42.7, 144.5) ➞ (-38.994, -3.706)

sum_and_product(10, 30) ➞ None
"""
import math

def sum_and_product(s, p):
    # Calculate a^2
    a_squared = s**2 - 4*p

    # Check if a^2 is negative
    if a_squared < 0:
        return None

    a = math.sqrt(a_squared)

    # Calculate x and y for positive 0
    # x1 = (s + a) / 2
    # y1 = (s - a) / 2

    # Calculate x and y for negative 0
    x2 = round((s - a) / 2, 3)
    y2 = round((s + a) / 2, 3)

    return (x2, y2)


print(sum_and_product(2, -15)) # ➞ (-3.0, 5.0)
print(sum_and_product(144, 144)) # ➞ (1.007, 142.993)
print(sum_and_product(-42.7, 144.5)) #, (-38.994, -3.706)),
print(sum_and_product(10, 30)) #, None),
print(sum_and_product(-11, 33)) # , None),
print(sum_and_product(-13, -99)) # , (-18.385, 5.385)),
print(sum_and_product(1111, 1234)) #, (1.112, 1109.888)),
print(sum_and_product(1234, 1111)) #, (0.901, 1233.099)),
print(sum_and_product(34, 289)) #, (17.0, 17.0)),
print(sum_and_product(-26.6, 176.89))# , (-13.3, -13.3)),
print(sum_and_product(0, -25)) #, (-5.0, 5.0)),
print(sum_and_product(0, 25)) # , None),
print(sum_and_product(-25, 0)) # , (-25.0, 0.0)),
print(sum_and_product(25, 0)) #, (0.0, 25.0)),
print(sum_and_product(0, 0)) #, (0.0, 0.0)),