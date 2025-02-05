import numpy as np

arr=np.array([3,4,5,6,7,8])

filtered_arr=[]

for i in arr:
    if i>4:
        filtered_arr.append(True)
    else:
        filtered_arr.append(False)
print(arr[filtered_arr])

#Another method

filtered_arr=arr>4
print(arr[filtered_arr])