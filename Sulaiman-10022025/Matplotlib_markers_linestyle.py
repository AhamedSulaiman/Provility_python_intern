import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([3, 8, 1, 10])

#Using the linestyle and the marrker
plt.plot(ypoints,linestyle=':' ,marker = 'o')
plt.show()

#Markersize and the marker color

plt.plot(ypoints,color='orange',linestyle='dotted' ,marker = 'o',ms=20,mec='r',mfc='green')
plt.show()

#Multiple lines

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()

