import random
import numpy as np
import matplotlib.pyplot as plt
from trying import ClassicFunctions

maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Create a 20x20 random array
g = ClassicFunctions(maze, 'gbfs', 1)
b = ClassicFunctions(maze, 'bfs')
d = ClassicFunctions(maze, 'dfs')
_, _, gh = g.returner()
_, _, bh = b.returner()
_, _, dh = d.returner()

if len(bh) > len(gh) < len(dh):
    print(gh)
    print('GH')
    # g.printing_out()
    g.printP(maze, g.get_best_path())
elif len(gh) > len(bh) < len(dh):
    print(bh)
    print("BH")
    # b.printing_out()
    b.printP(maze, b.get_best_path())

elif len(bh) > len(dh) < len(gh):
    print(dh)
    print("DH")
    # d.printing_out()
    d.printP(maze, d.get_best_path())
# v.printP(maze, b)
# for i in f:
#    print(i)
