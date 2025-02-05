import numpy as np

#Numpy Copy
print("Copy of the array ")
arr1=np.array([1,2,3,4,5])
x=arr1.copy()
arr1[3]=10
print(x)
print(arr1)

#Numpy View
print("View of the array")
arr1=np.array([1,2,3,4,5])
y=arr1.view()
arr1[3]=10
print(y)
print(arr1)

#Cheeck the base
print(x.base)
print(y.base)