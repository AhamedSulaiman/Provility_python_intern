#Set Accessing

fruits = {"apple", "banana", "cherry"}

for fruit in fruits:
  print(fruit)

#Checking the element in the set

print("banana" in fruits)

#Checking the element not in the set

print("Mango" not in fruits)

#Adding elements in the set

fruits.add("Mango")

print(fruits)

#updating te set

vegetables={"brinjal","peas"}

fruits.update(vegetables)
print(fruits)

#Removing element in the set

fruits.remove("brinjal")
print(fruits)

#pop function

new=fruits.pop()

print(new)
print(fruits)