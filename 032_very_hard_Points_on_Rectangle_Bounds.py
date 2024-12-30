"""
Points on Rectangle Bounds
Given a list of 2D points [x, y], create a function that returns True if those points can be on the bounds of a rectangle, False otherwise.



Examples
on_rectangle_bounds([[0, 1], [1, 0], [1, 1], [0, 0]]) ➞ True

on_rectangle_bounds([[0, 1], [1, 0], [1, 1], [0.5, 0.5]]) ➞ False

on_rectangle_bounds([[0, 1], [10, 0], [10, 1]]) ➞ True

on_rectangle_bounds([[0, 1]]) ➞ True
Notes
Only rectangles with sides parallel to x-axis and y-axis will be considered."""

def on_rectangle_bounds(points):

    if not points:
        return False
      
    # 入力された点からx座標とy座標を抽出
    x_cords = [point[0] for point in points]
    y_cords = [point[1] for point in points]
    
    # 各座標の最小値、最大値
    min_x, max_x = min(x_cords), max(x_cords)
    min_y, max_y = min(y_cords), max(y_cords)
    
    for x, y in points:
        if not (
            (x == min_x or x == max_x) and (min_y <= y <= max_y) or 
            (y == min_y or y == max_y) and (min_x <= x <= max_x)
        ):
          return False  
    return True


print(on_rectangle_bounds([[0,1]]))  # True, 'A point alone can be on the boundary of any rectangle')
print(on_rectangle_bounds([[0,1],[2,3]]))  # True)
print(on_rectangle_bounds([[0,1],[2,3],[0,5]]))  # True)
print(on_rectangle_bounds([[0,1],[2,3],[4,5]]))  # False)
print(on_rectangle_bounds([[0,1],[2,3],[4,5],[6,7]]))  # False)
print(on_rectangle_bounds([[1.94,0.0],[1.92,0.0],[1.99,0.0],[1.85,0.0],[0.56,0.0],[0.42,0.0],[0.35,0.0],[1.37,0.0],[0.91,0.0],[1.39,0.0],[0.02,0.0],[1.78,0.0],[1.63,0.0],[0.93,0.0],[1.92,0.0],[1.32,0.0],[0.73,0.0],[1.87,0.0],[1.48,0.0],[0.12,0.0]]))  # True)
print(on_rectangle_bounds([[2.0,-0.16],[2.0,-0.65],[2.0,1.0],[2.0,-0.43],[2.0,-0.84],[2.0,-0.15],[2.0,-0.29],[2.0,0.86],[2.0,0.89],[2.0,-0.17],[2.0,-0.69],[2.0,-0.95],[2.0,0.76],[2.0,-0.45],[2.0,0.8],[2.0,0.19],[2.0,-0.87],[2.0,-0.05],[2.0,-0.24],[2.0,0.95]]))  # True)
print(on_rectangle_bounds([[0.6,0.94],[0.74,1.18],[1.22,2.04],[1.1,1.21],[1.48,2.58],[0.19,3.78],[0.29,3.87],[0.9,1.4],[0.33,0.36],[0.49,2.67],[0.74,2.5],[1.87,3.64],[0.47,1.83],[1.39,3.89],[0.57,0.11],[1.75,1.07],[1.78,1.81],[1.9,2.51],[1.65,3.65],[0.05,3.78]]))  # False)
print(on_rectangle_bounds([[-1.12,-1.0],[-1.4,-1.0],[-0.97,-1.0],[-0.97,-1.0],[-1.61,-1.0],[-0.22,3.0],[-0.97,3.0],[-0.02,3.0],[-1.06,3.0],[-1.2,3.0],[-2.0,2.71],[-2.0,0.51],[-2.0,1.34],[-2.0,-0.84],[-2.0,-0.22],[2.0,3.28],[2.0,4.45],[2.0,3.79],[2.0,4.51],[2.0,4.77]]))  # False)
print(on_rectangle_bounds([[-1.01,-1.0],[-1.22,-1.0],[-1.44,-1.0],[-0.89,-1.0],[-0.1,-1.0],[-0.94,3.0],[-1.65,3.0],[-1.21,3.0],[-0.63,3.0],[-1.16,3.0],[-2.0,-0.57],[-2.0,-0.26],[-2.0,-0.27],[-2.0,-0.57],[-2.0,1.55],[2.0,2.79],[2.0,2.75],[2.0,2.85],[2.0,2.49],[2.0,2.73]]))  # True)
print(on_rectangle_bounds([[1.66,0.66],[0.02,-0.98],[0.87,-0.13],[1.87,0.87],[1.44,0.44],[0.19,-0.81],[1.92,0.92],[0.84,-0.16],[0.71,-0.29],[0.31,-0.69],[1.25,0.25],[0.76,-0.24],[0.58,-0.42],[0.53,-0.47],[0.37,-0.63],[0.04,-0.96],[0.71,-0.29],[1.68,0.68],[0.82,-0.18],[1.94,0.94]]))  # False)
print(on_rectangle_bounds([[0.19,-0.81],[1.89,0.89],[1.17,0.17],[1.82,0.82],[1.84,0.84],[1.74,0.74],[1.92,0.92],[0.09,-0.91],[1.66,0.66],[1.83,0.83],[0.29,-0.71],[0.84,-0.16],[1.95,0.95],[1.68,0.68],[0.56,-0.44],[1.97,0.97],[1.09,0.09],[0.23,-0.77],[1.13,0.13],[1.24,0.24],[-1.03,1.03],[-0.74,0.74],[-0.39,0.39],[-0.04,0.04],[-1.24,1.24],[-0.91,0.91],[-0.94,0.94],[-0.68,0.68],[-1.51,1.51],[-1.96,1.96],[-0.34,0.34],[-1.75,1.75],[-1.53,1.53],[-0.66,0.66],[-1.28,1.28],[-0.68,0.68],[-1.47,1.47],[-0.36,0.36],[-0.38,0.38],[-0.48,0.48]]))  # False)
print(on_rectangle_bounds([[2.69,-1.0],[0.95,-1.0],[3.68,-1.0],[-0.79,-1.0],[2.42,-1.0],[1.85,-1.0],[-0.3,-1.0],[-0.25,-1.0],[3.51,-1.0],[0.83,-1.0],[1.45,-1.0],[1.13,-1.0],[1.74,-1.0],[0.08,-1.0],[2.33,-1.0],[0.31,-1.0],[1.89,-1.0],[2.24,-1.0],[-1.94,-1.0],[-1.19,-1.0],[1.49,3.0],[0.28,3.0],[0.12,3.0],[-1.97,3.0],[1.94,3.0],[-0.96,3.0],[-1.74,3.0],[-1.59,3.0],[0.19,3.0],[-1.33,3.0],[0.53,3.0],[0.12,3.0],[0.83,3.0],[0.42,3.0],[-0.13,3.0],[1.41,3.0],[-1.65,3.0],[0.93,3.0],[0.75,3.0],[-0.21,3.0],[-2.0,1.52],[-2.0,0.75],[-2.0,2.96],[-2.0,1.5],[-2.0,2.35],[-2.0,0.11],[-2.0,0.42],[-2.0,-0.42],[-2.0,-0.03],[-2.0,1.7],[-2.0,0.05],[-2.0,0.76],[-2.0,1.56],[-2.0,1.51],[-2.0,2.22],[-2.0,2.82],[-2.0,0.65],[-2.0,2.73],[-2.0,1.44],[-2.0,-0.51],[2.0,1.01],[2.0,-0.7],[2.0,0.7],[2.0,1.35],[2.0,2.84],[2.0,-0.02],[2.0,0.3],[2.0,-0.81],[2.0,1.66],[2.0,0.9],[2.0,2.3],[2.0,-0.12],[2.0,-0.77],[2.0,0.64],[2.0,-0.35],[2.0,0.54],[2.0,-0.08],[2.0,2.05],[2.0,1.03],[2.0,-0.17]]))  # False)
print(on_rectangle_bounds([[-0.08,-1.0],[0.37,-1.0],[0.56,-1.0],[-1.32,-1.0],[-1.76,-1.0],[0.56,-1.0],[0.6,-1.0],[1.94,-1.0],[-0.42,-1.0],[1.66,-1.0],[0.9,-1.0],[0.79,-1.0],[0.24,-1.0],[1.13,-1.0],[-1.89,-1.0],[-0.6,-1.0],[1.5,-1.0],[-1.34,-1.0],[-0.95,-1.0],[1.96,-1.0],[1.17,3.0],[-0.87,3.0],[-0.45,3.0],[1.82,3.0],[-0.5,3.0],[0.56,3.0],[-1.95,3.0],[1.42,3.0],[0.98,3.0],[0.24,3.0],[-0.41,3.0],[1.32,3.0],[1.48,3.0],[-0.5,3.0],[0.64,3.0],[-1.63,3.0],[-0.23,3.0],[0.62,3.0],[-0.58,3.0],[-1.37,3.0],[-2.0,1.06],[-2.0,1.24],[-2.0,2.31],[-2.0,-0.6],[-2.0,0.75],[-2.0,1.33],[-2.0,-0.49],[-2.0,-0.87],[-2.0,-0.56],[-2.0,0.1],[-2.0,2.4],[-2.0,-0.65],[-2.0,1.36],[-2.0,2.1],[-2.0,-0.53],[-2.0,1.53],[-2.0,0.9],[-2.0,2.67],[-2.0,1.67],[-2.0,0.02],[2.0,-0.67],[2.0,2.48],[2.0,-0.77],[2.0,-0.99],[2.0,-0.53],[2.0,2.88],[2.0,1.13],[2.0,0.73],[2.0,1.93],[2.0,-0.93],[2.0,0.53],[2.0,0.29],[2.0,2.99],[2.0,0.12],[2.0,0.08],[2.0,-0.77],[2.0,2.44],[2.0,-0.74],[2.0,1.07],[2.0,0.67]]))  # True)
print(on_rectangle_bounds([[-0.64,-1.0],[-1.4,-1.0],[-1.51,-1.0],[-1.64,-1.0],[-1.34,-1.0],[-1.78,-1.0],[-1.96,-1.0],[-0.97,-1.0],[-0.46,-1.0],[-1.51,-1.0],[-0.63,-1.0],[-1.86,-1.0],[-0.85,-1.0],[-0.15,-1.0],[-1.49,-1.0],[-1.52,-1.0],[-1.3,-1.0],[-1.85,-1.0],[-0.21,-1.0],[-0.92,-1.0],[1.56,3.0],[-1.62,3.0],[0.93,3.0],[-1.23,3.0],[0.77,3.0],[-1.59,3.0],[-1.46,3.0],[-0.85,3.0],[0.28,3.0],[1.32,3.0],[0.29,3.0],[-0.37,3.0],[-1.2,3.0],[-1.03,3.0],[1.4,3.0],[-0.8,3.0],[1.87,3.0],[-0.79,3.0],[0.53,3.0],[1.2,3.0],[-2.0,-0.51],[-2.0,0.11],[-2.0,0.55],[-2.0,0.02],[-2.0,1.83],[-2.0,1.69],[-2.0,2.16],[-2.0,1.54],[-2.0,0.91],[-2.0,0.77],[-2.0,2.05],[-2.0,0.14],[-2.0,1.42],[-2.0,1.76],[-2.0,0.59],[-2.0,-0.14],[-2.0,1.65],[-2.0,1.03],[-2.0,0.13],[-2.0,0.57],[2.0,2.59],[2.0,2.77],[2.0,2.84],[2.0,2.01],[2.0,2.54],[2.0,2.4],[2.0,2.92],[2.0,2.8],[2.0,2.63],[2.0,2.28],[2.0,2.37],[2.0,2.89],[2.0,2.68],[2.0,2.28],[2.0,2.4],[2.0,2.77],[2.0,2.78],[2.0,2.55],[2.0,2.61],[2.0,2.94]]))  # True)
print(on_rectangle_bounds([[-1.18,-1.0],[2.12,-1.0],[2.48,-1.0],[3.01,-1.0],[2.85,-1.0],[-0.62,-1.0],[0.38,-1.0],[2.12,-1.0],[3.42,-1.0],[1.2,-1.0],[1.72,-1.0],[2.33,-1.0],[2.27,-1.0],[0.23,-1.0],[1.23,-1.0],[3.91,-1.0],[2.3,-1.0],[1.29,-1.0],[-0.64,-1.0],[-0.4,-1.0],[0.49,3.0],[1.44,3.0],[0.19,3.0],[1.35,3.0],[-0.95,3.0],[-1.49,3.0],[0.17,3.0],[0.31,3.0],[0.9,3.0],[1.25,3.0],[-0.31,3.0],[-1.58,3.0],[-1.31,3.0],[0.54,3.0],[1.14,3.0],[-1.35,3.0],[-0.38,3.0],[0.55,3.0],[0.94,3.0],[-1.88,3.0],[-2.0,2.7],[-2.0,2.89],[-2.0,2.39],[-2.0,2.02],[-2.0,-0.85],[-2.0,1.61],[-2.0,-0.3],[-2.0,1.39],[-2.0,-0.59],[-2.0,0.58],[-2.0,2.6],[-2.0,1.54],[-2.0,-0.18],[-2.0,-0.8],[-2.0,0.82],[-2.0,1.07],[-2.0,0.65],[-2.0,2.67],[-2.0,2.72],[-2.0,2.39],[2.0,-0.97],[2.0,-0.19],[2.0,-1.73],[2.0,-1.89],[2.0,-1.57],[2.0,-0.8],[2.0,-0.43],[2.0,-0.26],[2.0,0.33],[2.0,-2.38],[2.0,0.87],[2.0,-1.46],[2.0,-0.55],[2.0,-2.32],[2.0,-2.09],[2.0,0.51],[2.0,-1.88],[2.0,-0.91],[2.0,0.89],[2.0,-1.27]]))  # False)
print(on_rectangle_bounds([[-1.06,-1.0],[-0.9,-1.0],[-1.16,-1.0],[-0.78,-1.0],[-0.15,-1.0],[-0.76,-1.0],[-1.23,-1.0],[-1.55,-1.0],[-0.91,-1.0],[-1.62,-1.0],[-1.02,-1.0],[-0.88,-1.0],[-0.57,-1.0],[-2.0,-1.0],[-0.11,-1.0],[-1.57,-1.0],[-1.05,-1.0],[-1.52,-1.0],[-0.86,-1.0],[-0.87,-1.0],[1.75,3.0],[-0.91,3.0],[1.14,3.0],[-1.09,3.0],[0.53,3.0],[0.82,3.0],[-1.51,3.0],[1.28,3.0],[1.41,3.0],[0.89,3.0],[-0.46,3.0],[-1.92,3.0],[-1.67,3.0],[-1.83,3.0],[1.02,3.0],[1.79,3.0],[-0.1,3.0],[-0.56,3.0],[-0.27,3.0],[0.56,3.0],[-2.0,-0.5],[-2.0,-0.19],[-2.0,2.95],[-2.0,2.28],[-2.0,1.05],[-2.0,0.78],[-2.0,1.07],[-2.0,-0.57],[-2.0,2.4],[-2.0,-0.01],[-2.0,-0.15],[-2.0,0.06],[-2.0,0.93],[-2.0,0.36],[-2.0,0.64],[-2.0,2.28],[-2.0,-0.97],[-2.0,0.53],[-2.0,-0.94],[-2.0,-0.23],[2.0,2.88],[2.0,1.85],[2.0,-0.77],[2.0,1.55],[2.0,0.65],[2.0,2.25],[2.0,0.45],[2.0,1.13],[2.0,0.45],[2.0,-0.86],[2.0,2.04],[2.0,0.72],[2.0,2.17],[2.0,-0.78],[2.0,0.6],[2.0,-0.28],[2.0,2.28],[2.0,2.77],[2.0,1.06],[2.0,2.26]]))  # True)
print(on_rectangle_bounds([[-0.52,-1.0],[-0.26,-1.0],[-0.13,-1.0],[-0.51,-1.0],[-0.17,-1.0],[-1.88,-1.0],[-0.99,-1.0],[-0.43,-1.0],[-0.04,-1.0],[-1.13,-1.0],[-0.76,-1.0],[-0.91,-1.0],[-0.13,-1.0],[-0.3,-1.0],[-1.83,-1.0],[-0.57,-1.0],[-1.65,-1.0],[-1.09,-1.0],[-0.27,-1.0],[-1.73,-1.0],[-0.26,3.0],[-0.9,3.0],[-1.61,3.0],[-0.72,3.0],[-0.11,3.0],[-1.95,3.0],[-0.62,3.0],[-1.19,3.0],[-0.75,3.0],[-0.4,3.0],[-1.59,3.0],[-0.44,3.0],[-0.32,3.0],[-0.22,3.0],[-1.69,3.0],[-1.71,3.0],[-0.58,3.0],[-1.15,3.0],[-1.32,3.0],[-0.07,3.0],[-2.0,-0.41],[-2.0,0.83],[-2.0,1.27],[-2.0,2.45],[-2.0,1.85],[-2.0,-0.71],[-2.0,2.72],[-2.0,0.15],[-2.0,2.49],[-2.0,2.69],[-2.0,0.49],[-2.0,0.91],[-2.0,0.11],[-2.0,1.54],[-2.0,-0.48],[-2.0,0.13],[-2.0,2.79],[-2.0,2.66],[-2.0,-0.49],[-2.0,1.18],[2.0,2.36],[2.0,2.41],[2.0,2.1],[2.0,2.98],[2.0,2.48],[2.0,2.11],[2.0,2.61],[2.0,2.52],[2.0,2.88],[2.0,2.01],[2.0,2.41],[2.0,2.22],[2.0,2.16],[2.0,2.14],[2.0,2.46],[2.0,2.99],[2.0,2.92],[2.0,2.75],[2.0,2.65],[2.0,2.57]]))  # True)
  
  
  