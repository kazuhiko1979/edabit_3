"""
We Have a House
In the garden, we have a house. We don't know how big the house is going to get. The garden is 50' x 50'. If you want to walk around the house, you'll need 3 feet so the house cannot be bigger than the width & depth of the garden minus the path to walk around it.

We Have a House

In this example you can see the arguments your function is going to get (in red). The measurements of the windows + door as well as the dark rim (against rain damage) are always the same (in blue). We put One door in the front and Two windows in each wall.

We don't have permission to build higher than 20'. The area around the windows and door cannot be smaller than 1 foot except under the door obviously. It is possible to have a flat roof.

Create a function that takes four arguments and returns the area of light yellow paint and dark gray paint in a string as square feet. Assuming the coverage of the paint is perfect and you'll only need one layer of paint.

Examples
we_have_house(8, 30, 32, 8) ➞ "Yellow: 873, Gray: 242"

we_have_house(9, 14, 20, 9) ➞ "House too small."

we_have_house(9, 38, 36, 9) ➞ "Yellow: 1261, Gray: 290"

we_have_house(10, 31, 30, 11) ➞ "No permission."
Notes
If the house is too big for the garden, return "House too big."
If the house is too high, return "No permission."
If the house is too small (for the windows and door to fit)) # return "House too small."
"""

def we_have_house(h, w, d, r):
    # 1. 家のサイズ制約をチェック
    max_size = 44  # 庭 50' x 50' から 3' の通路を引いた最大サイズ
    if w > max_size or d > max_size:
        return "House too big."

    # 2. 高さ制約をチェック
    if h  + r > 20:
        return "No permission."

    # 3. 最小サイズ制約をチェック
    min_height = 8  # 窓とドアのために最低必要な高さ
    min_width = 15  # ドアと窓を配置するための最小幅
    min_depth = 11  # 窓を配置するための最小奥行き
    if h < min_height or w < min_width or d < min_depth:
        return "House too small."

    # 4. 塗装面積を計算
    gray_area = 4 * (w + d) - 6 # 1 フィートのリム x 4 辺 

    opening_area = (8 * 12 + 21)

    # 黄色のペイント（壁の面積から開口部を引く）
    yellow_area = (w * r) + (2 * h * (w + d)) - opening_area - gray_area

    # 5. 結果を返す
    return "Yellow: {}, Gray: {}".format(yellow_area, gray_area)


# テスト
print(we_have_house(8, 30, 32, 8))  # "Yellow: 873, Gray: 242"
print(we_have_house(10, 31, 30, 11))  # "No permission."
print(we_have_house(8, 30, 30, 8))  # "Yellow: 849, Gray: 234"
print(we_have_house(9, 20, 18, 8))  # "Yellow: 581, Gray: 146"
print(we_have_house(9, 14, 20, 9))  # "House too small."
print(we_have_house(8, 16, 12, 8))  # "Yellow: 353, Gray: 106"
print(we_have_house(10, 25, 25, 0))  # "Yellow: 689, Gray: 194"
print(we_have_house(8, 45, 42, 8))  # "House too big."
print(we_have_house(10, 40, 40, 10))  # "Yellow: 1569, Gray: 314"
print(we_have_house(10, 15, 10, 7))  # "House too small."
print(we_have_house(9, 38, 36, 9))  # "Yellow: 1267, Gray: 290"
print(we_have_house(8, 15, 12, 6))  # "Yellow: 303, Gray: 102"
print(we_have_house(8, 30, 45, 6))  # "House too big."
print(we_have_house(9, 20, 14, 8))  # "Yellow: 525, Gray: 130"