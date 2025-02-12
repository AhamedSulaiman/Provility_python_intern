#Using lambda function in the list

a=[5,10,45,72,65,87,93]
vals=list(sorted(filter(lambda x:x>=50,a)))
print(vals)


#lambda function to take any number as the argument
pow=lambda x,y:x**y
print(pow(2,4))

#lambda function inside the user defined function

def mul(n):
    return lambda x:x*n

a=mul(5)
print(a(5))


nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums,))
print(squared)


#Using the map function
list1 = [1, 2, 3]
list2 = [4, 5, 6]

sum_list = list(map(lambda x, y: x + y, list1, list2))

print(sum_list)