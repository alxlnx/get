#!/usr/bin/python3
import numpy as np
from matplotlib import pyplot as plt

# np.zeros(3)
# np.ones(3)
# np.random.random(3)
# np.ones(3, dtype=np.int64)
# np.empty(3)
# 
# ones = np.ones(2, dtype=np.int32)
# data = np.array([1, 2], dtype=np.int32)
# ones + data
# ones * data  # Must have equal length
# 
# data * 1.6  # Broadcasting: each num * 1.6
# 
# matrix = np.array( [ [1,2], [3, 4], [5, 6] ] ) 
# #  matrix[row, column]
# # np.ones((3,2))  # 3 rows, 2 cols filled with 1 (not E)
# matrix * matrix  # Broadcasting, NOT usual matrix muplt using dot-product
# # matrix.dot(matrix)  # There it is
# np.ones(1, 2, 3)  # 1 row, 2 cols, 3 layers
# 
# matrix.ndim  # dim count
# matrix.size
# matrix.shape  # (3,2) - r, c, layers
# 
# np.arange(4)  # 0, 1, 2, 3
# # np.arange(START, STOP, STEP)
# np.linspace(0, 10, num=5) # split [0, 10] in five steps and assign
# # 0, 2.5, 5, 7.5, 10
# 
# data.max()
# data.min()
# data.sum()
# np.save('filename', data) # npy file
# arr = np.load('filename.npy')
# 
# MATPLOTLIB
# with open('settings.txt', 'r') as settings:
#   tmp = [float[i] for i in settings.read().split('\n') ]

data_array = np.loadtxt('data.txt', dtype=int)

# figure -> axes -> ...

fig, ax = plt.subplots(figsize=(16,10), dpi=400)  # figure, axes
# width, height
# nrows = how many axeses (graphs) on one fig
ax.plot(data_array)
fig.savefig('test.png')
# axes has lots of cool methods
plt.show()
