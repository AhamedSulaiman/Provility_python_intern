#Importing matplotlib and numpy Libraries
import matplotlib.pyplot as plt
import numpy as np

#Giving the values for the x and y axis
x=np.array([0,25])
y=np.array([0,40])

#Giving the title for the figure
plt.title("Employee Details")

#Giving labels for the x and y
plt.xlabel('Age')
plt.ylabel("Salaray in LPA")

plt.plot(x,y)

plt.show()


#Giving the values for the x and y axis
x=np.array([0,25])
y=np.array([0,40])


#creating the dictionary to be inserted in the fontdict
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#Using the fontdict parameter in the title
plt.title("Employee details",fontdict=font1)

#Using the fontdict parameter in teh xlabel and the ylabel
plt.xlabel('Age',fontdict=font2)
plt.ylabel("Salaray in LPA",fontdict=font2)

plt.plot(x,y)

plt.show()

#Using grid function to add gird lines to the plot

#creating the dictionary to be inserted in the fontdict
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#Using the fontdict parameter in the title
plt.title("Employee details",fontdict=font1)

#Using the fontdict parameter in teh xlabel and the ylabel
plt.xlabel('Age',fontdict=font2)
plt.ylabel("Salaray in LPA",fontdict=font2)

#Using grid function to add gird lines to the plot
plt.grid()

plt.plot(x,y)

plt.show()

#using parameters like colors,linestyle,linewidth in the grid function
plt.grid(color="green",linestyle=":",linewidth=0.5)

plt.plot(x,y)
plt.show()