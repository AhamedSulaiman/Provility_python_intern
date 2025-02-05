import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])

#concatination function
print("Concatination fuction")
arr=np.concatenate((arr1,arr2))
print(arr)
print("Concatination fuction in 2D")
arr3=np.array([[1,2,3],[4,5,6]])
arr4=np.array([[7,8,9],[10,11,12]])
arr=np.concatenate((arr3,arr4),axis=1)
print(arr)

#Stack function
print("Stack Function")
arr=np.stack((arr1,arr2),axis=1)
print(arr)

#hstack function
print("hstack function")
arr=np.hstack((arr1,arr2))
print(arr)

#vstack function
print("vstack")
arr=np.vstack((arr1,arr2))
print(arr)