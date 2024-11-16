"""
Triangle Challenge
Given the perimeter and the area of a triangle, devise a function that returns the length of the sides of all triangles that fit those specifications. The length of the sides must be integers. Sort results in ascending order.

triangle(perimeter, area) ➞ [[s1, s2, s3]]
Examples
triangle(12, 6) ➞ [[3, 4, 5]]

triangle(45, 97.42786) ➞ [[15, 15, 15]]

triangle(70, 210) ➞ [[17, 25, 28], [20, 21, 29]]

triangle(3, 0.43301) ➞ [[1, 1, 1]]
Notes
Area is rounded to hundred thousandth (5 decimal places).
e.g. 59.444441 would round to 59.44444.
"""

def calculate_area(a, b, c):
    """ using a Helon formula """
    s = (a + b + c) / 2
    if s <= a or s <= b or s <= c:
        return 0
    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
    return round(area, 5)

def triangle(perimeter, area):

    solutions = []
    max_side = perimeter // 2

    for c in range(1, max_side + 1):
        remaining = perimeter - c

        for b in range((remaining - 1) // 2 + 1, min(remaining, c + 1)):
            a = remaining - b

            if a <= 0 or a + b <= c:
                continue

            calculated_area = calculate_area(a, b, c)
            if abs(calculated_area - area) < 0.00001:
                solutions.append([a, b, c])

    return sorted(solutions)


print(triangle(3, 0.43301)) #, [[1, 1, 1]])
print(triangle(201, 49.99937)) #, [[1, 100, 100]])
print(triangle(98, 420)) #, [[24, 37, 37], [25, 34, 39], [29, 29, 40]])
print(triangle(70, 210)) #, [[17, 25, 28], [20, 21, 29]])
print(triangle(30, 30)) #, [[5, 12, 13]])
print(triangle(1792, 55440)) #, [[170, 761, 861], [291, 626, 875]])
print(triangle(150, 420)) #, [[26, 51, 73]])
print(triangle(864, 23760)) #, [[132, 366, 366], [135, 352, 377]])







