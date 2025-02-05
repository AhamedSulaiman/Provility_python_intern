import numpy as np

print("One Dimensional indexing ")
#positive indexing
arr1=np.array([1,2,3,4,5])
print(arr1[0])

print(arr1[0]+arr1[4])

#negative indexing
print(arr1[-1])

#2D indexing
print("Two Dimensional indexing")
arr2=np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(arr2[0,2])
print(arr2[0,2]+arr2[1,4])

#3D indexing
print("Three dimensional indexing")

arr3=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
print(arr3[0,1,-1])
