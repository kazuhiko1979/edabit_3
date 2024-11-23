"""
Cinemas in 2021
Given a list of seats, return the maximum number of new people which can be seated, as long as there is at least a gap of 2 seats between people.

Empty seats are given as 0.
Occupied seats are given as 1.
Don't move any seats which are already occupied, even if they are less than 2 seats apart. Consider only the gaps between new seats and existing seats.
Examples
maximum_seating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0]) ➞ 2
# [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]

maximum_seating([0, 0, 0, 0]) ➞ 2
# [1, 0, 0, 1]

maximum_seating([1, 0, 0, 0, 0, 1]) ➞ 0
# There is no way to have a gap of at least 2 chairs when adding someone else.
"""


def maximum_seating(seats):

    available_seat = 0

    for i in range(0, len(seats)):
        if seats[i] == 0:
            # 左側の2つの席が空いているかを確認
            # i - 1 と i - 2 がリストの範囲外にならないようにする
            left_clear = True
            if i - 1 >= 0 and seats[i - 1] == 1:
                left_clear = False
            if i - 2 >= 0 and seats[i - 2] == 1:
                left_clear = False

            # 右側の2つの席が空いているかを確認
            # i + 1 と i + 2 がリストの範囲外にならないようにする
            right_clear = True
            if i + 1 < len(seats) and seats[i + 1] == 1:
                right_clear = False
            if i + 2 < len(seats) and seats[i + 2] == 1:
                right_clear = False

            # 左右両方の条件を満たしていれば、この席に座れる
            if left_clear and right_clear:
                seats[i] = 1
                available_seat += 1

    # print(seats)
    return available_seat


print(maximum_seating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0])) #, 2)
print(maximum_seating([0, 0, 0, 0])) #, 2)
print(maximum_seating([1, 0, 0, 0, 0, 0, 1])) #, 1)
print(maximum_seating([1, 0, 0, 0, 0, 0, 0, 1])) #, 1)
print(maximum_seating([1, 0, 0, 0, 0, 1])) #, 0, "Remember to keep a 2 chair gap on both sides!")
print(maximum_seating([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) #, 4)
print(maximum_seating([0])) #, 1)
print(maximum_seating([0, 0])) #, 1)
print(maximum_seating([1])) #, 0)
print(maximum_seating([0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0])) #, 1)
