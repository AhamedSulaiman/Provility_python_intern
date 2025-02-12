import math

#Built-in math function

a=min(1,2,3,4,6)
b=max(1,2,3,4,6)

print(f"The min and max value of the elements are {a} and {b}")
print()

c=-567
x=abs(c)
print(f"The absolute value of {c} is {x}")
print()

a=pow(4,2)
print(f"The power of 4,2 is {a}")
print()

#To get the pi value
x=71
y=math.sqrt(x)
#Using the sqrt function to get the square root of the particular value
print(f"The Square root of {x} is {y}")
print()

p=math.pi
#Using the math.pi to get the pi value
print(f"The value of pi is {p}")
print()

#Using ceil and floor function
x=1.45
print(f"The number upward to its nearest integer is {math.ceil(x)}")
print(f"The number downwards to its nearest integer is {math.floor(x)}")
print()

#Area of the circle
r=5
print(f"The area of the circle is {p*r*r}")