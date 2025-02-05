import numpy as np

#Iteerate 1D array
print("Iterating 1D array")
arr1 = np.array([1, 2, 3])

for x in arr1:
  print(x)

#Iterate 2D array
print("Iterating 2D array")
arr2=np.array([[1,2,3],[4,5,6]])

for x in arr2:
    for y in x:
        print(y)


#Iterate 3D array
print("Iterating 3D array")
arr3=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
for x in arr3:
    for y in x:
        for z in y:
            print(z)

#Interate using nditer() function
print("Iterating using nditer() function")
arr3=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
for x in np.nditer(arr3):
    print(x)
print("using slicing operater")
for x in np.nditer(arr3[1:,1:, ::2]):
    print(x)



print("Iterating using Enumerate function")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
