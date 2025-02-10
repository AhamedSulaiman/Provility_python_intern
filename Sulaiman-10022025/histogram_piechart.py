import matplotlib.pyplot as plt
import numpy as np

#Histogram

x = np.random.normal(170, 10, 250)

plt.hist(x,color='r')
plt.show()

#Pie chart
explodes=[0,0,0,0,0.2]
x=np.array([50,10,10,25,5])
label=np.array(["Maths","English","Tamil","Social","Science"])

plt.title("Fail list")
plt.pie(x,labels=label,autopct='%1.1f%%',explode=explodes,shadow=True)

plt.legend()

plt.show()
