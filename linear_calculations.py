"""
Name: Ruby Koehler
Date: 1/7/25
Description:
"""
import math

def slope(point1:tuple,point2:tuple)->float:
    x1 = point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2 = point2[1]
    dx = x2-x1 # change in x
    dy = y2-y1 # change in y
    slope = dy/dx
    return slope

def distance(point1:tuple, point2:tuple)->float:
    x1 = point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2 = point2[1]
    dx = x2 - x1  # change in x
    dy = y2 - y1  # change in y
    dist = math.sqrt(dx**2 + dy**2)
    return dist

def main():
    point1 = (3,4)
    point2 = (-8, 12)
    print(slope(point1,point2))
    print(distance(point1, point2))

if __name__ == "__main__":
    main()
