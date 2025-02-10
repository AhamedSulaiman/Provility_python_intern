#Importing matplotlib and numpy Libraries
import matplotlib.pyplot as plt
import numpy as np

#Giving the values for the x and y axis
x=np.array([0,25])
y=np.array([0,30])


plt.plot(x,y,'o')

plt.show()


#Multiple points

x=np.array([1,2,4,32,35])
y=np.array([3,1,30,12,21])

plt.plot(x,y)
plt.show()

#Default x values

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()