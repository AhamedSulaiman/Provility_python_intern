import matplotlib.pyplot as plt
import numpy as np

#Scatter Plot 1
x=np.array([1,2,5,7,18,21,50])
y=np.array([4,6,7,8,12,15,30])

plt.scatter(x,y)

#Scatter plot 2
x=np.array([32,4,5,65,41,10,11])
y=np.array([11,1,5,7,53,12,89])

plt.scatter(x,y)

plt.show()

#coloring each dots
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x,y,c=colors)

plt.colorbar()

plt.show()

#Using alpha and size function

x=np.random.randint(100,size=100)
y=np.random.randint(100,size=100)
colors=np.random.randint(100,size=100)
size=10*np.random.randint(100,size=100)

plt.scatter(x,y,c=colors,s=size,alpha=0.5,cmap='nipy_spectral')

plt.colorbar()

plt.show()