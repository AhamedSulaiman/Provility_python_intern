#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x[0]]

print(newlist)

#
newlist = [x*2 for x in range(10)]

print(newlist)