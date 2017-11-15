import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
xs = np.arange(0, 5, 5/40.)
ys = np.arange(0, 5, 5/40.)
xv, yv = np.meshgrid (xs, ys)
zv = np.zeros((40,40))
ax = plt.gca(projection='3d')
ax.contour(xv, yv, zv, zdir='x')
plt.show()