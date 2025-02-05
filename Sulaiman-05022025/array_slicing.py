import numpy as np

#1D array slicing
arr1=np.array([1,2,3,4,5])
print(arr1[:3])

#2d array slicing
arr2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2[:2,:3])

#3D array slicing
arr3=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
print(arr3[:,:,:3])