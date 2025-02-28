"""
Hexadecimal Color Mixer
In this challenge, you have to mix two or more colors to get a brand new color from their average rgb values.

Each color will be represented in its hexadecimal notation, and so as a string starting with # containing three pairs of alphanumeric characters, equals to the three rgb values (in base 16) of red, green and blue.

To obtain the new color, you need to get the arithmetic average of the sums of the individual red, green and blue values of each given color. When the average is a float number, you have to round it to the nearest integer (rounding up for decimal parts equal to 0.5).

Mixing yellow and red:

Hexadecimal code of yellow = "#FFFF00"
Hexadecimal code of red = "#FF0000"

yellow to RGB = Red: ["FF" = 255], Green: ["FF" = 255], Blue: ["00", 0]
red to RGB = Red: ["FF" = 255], Green: ["00" = 0], Blue: ["00" = 0]

Average of Red values = (255 + 255) / 2 = 255
Average of Green values = (255 + 0) / 2 = 127.5 = 128
Average of Blue values = (0 + 0) / 2 = 0 = 0

Rgb of new color = [255, 128, 0]
Hexadecimal conversion = [255 = "FF"], [128 = "80"], [0 = "00"]

New color = "#FF8000" (orange)
Given a list of strings colors containing a series of hexadecimal codes, implement a function that returns the hexadecimal code of the new color, as a new string.

Examples
hex_color_mixer(["#FFFF00", "#FF0000"]) ➞ "#FF8000"
# Orange

hex_color_mixer(["#FFFF00", "#0000FF"]) ➞ "#808080"
# Medium gray

hex_color_mixer(["#B60E73", "#0EAEB6"]) ➞ "#625E95"
# Lavender
Notes
Remember to round to the nearest integer the average of the rgb values.
You can test the color codes in any hexadecimal-colors utility site, such as this one that I used for testing cases.
All the given hexadecimal strings are valid; there are no exceptions to handle.
"""
def hex_color_mixer(colors):
    
    total_r, total_g, total_b = 0, 0, 0

    for color in colors:
        color = color.lstrip('#')
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        total_r += r
        total_g += g
        total_b += b

    avg_r = int(total_r / len(colors) + 0.5)
    avg_g = int(total_g / len(colors) + 0.5)
    avg_b = int(total_b / len(colors) + 0.5)

    return "#{:02X}{:02X}{:02X}".format(avg_r, avg_g, avg_b)


print(hex_color_mixer(["#FFFF00", "#FF0000"])) # "#FF8000", "Example #1")
print(hex_color_mixer(["#FFFF00", "#0000FF"])) # "#808080", "Example #2")
print(hex_color_mixer(["#B60E73", "#0EAEB6"])) # "#625E95", "Example #3")
print(hex_color_mixer(["#FF0000", "#00FF00", "#0000FF"])) # "#555555")
print(hex_color_mixer(["#99CC00", "#663399", "#1A8191"])) # "#5E8063")
print(hex_color_mixer(["#918381", "#D53B21", "#A54C83", "#DEFACF"])) # "#BA817D")
print(hex_color_mixer(["#140A23", "#46B31E", "#CFDF08", "#263534", "#EAD1FB", "#235E02"])) # "#65803F")
print(hex_color_mixer(["#FFFFFF", "#000000", "#000000", "#FFFFFF"])) # "#808080")
print(hex_color_mixer(["#CCCCCC"])) # "#CCCCCC")
    
    

