list1="[x**2 for x in range(1,6)]"

print(eval(list1))
print()

#Calling the function dynamically

def square(n):
    return n * n

result = eval("square(7)")
print(result)
print()


expr = "5 * (10 + 2) / 4"
result = eval(expr)
print(result)
