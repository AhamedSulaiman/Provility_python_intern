import numpy as np

#Checking the dataType
arr1=np.array([1,2,3,4,5])
print(arr1.dtype)

arr2=np.array(["Sulaiman","Ahamed","MA"])
print(arr2.dtype)

#Converting data on existing data Arrays
arr1=np.array([1,2,3,4,5])
print(arr1.astype(str))

arr = np.array([1.1, 2.1, 3.1])
print(arr.astype(int))

