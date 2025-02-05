import numpy as np

#To check the shape of the particular array
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr.shape)

arr1=np.array([1,2,3,4,5],ndmin=5)
print(arr1.shape)

#Reshape the array

arr1=np.array([1,2,3,4,5,6])

print(arr1.reshape(2,3))

#Flattening the arrays

print(arr1.reshape(-1))


