#Importing matplotlib and numpy Libraries
import matplotlib.pyplot as plt
import numpy as np

#Giving the values for the x and y axis
x=np.array([0,25])
y=np.array([0,40])

#Giving the title for the figure
plt.title("Employee Details")

#Giving labels for the x and y
# plt.xlabel('Age')
# plt.ylabel("Salaray in LPA")
plt.subplot(2,1,1)
plt.plot(x,y)




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

plt.subplot(2,1,2)
plt.plot(x,y)

plt.show()