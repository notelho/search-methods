import sys

sys.setrecursionlimit(100000)

from classes.breadth_first import BreadthFirst

a =  BreadthFirst([[1, 2, 3], ['x', 8, 4], [7, 6, 5]], [[1, 2, 3], [8, 'x', 4], [7, 6, 5]])

# search = BreadthFirst([[1, 2, 3], ['x', 8, 4], [7, 6, 5]], [[1, 2, 3], [8, 'x', 4], [7, 6, 5]])
