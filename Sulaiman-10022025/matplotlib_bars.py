import matplotlib.pyplot as plt
import numpy as np

#Vertical boxplot

x=np.array(["Eng","Maths","Science","Social Science","Tamil"])
y=np.array([75,68,90,45,34])

plt.xlabel("Subject")
plt.ylabel("Marks")

plt.title("Student Marks")


plt.bar(x,y)

plt.show()


#Horizontal Barplot

x=np.array(["Eng","Maths","Science","Social Science","Tamil"])
y=np.array([75,68,90,45,34])

plt.xlabel("Subject")
plt.ylabel("Marks")

plt.title("Student Marks")


plt.barh(x,y)

plt.show()