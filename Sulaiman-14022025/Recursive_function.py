def fibonacci(n):
    if n == 0:  # Base case 1
        return 0
    elif n == 1:  # Base case 2
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call

print(fibonacci(6))

def sum_of_series(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return (n)+ sum_of_series(n-1)
print("The sum of the series:")
print(sum_of_series(10))

def sum_of_squared_series(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return (n**2)+ sum_of_squared_series(n-1)
print("the sum of the square of the series:")
print(sum_of_squared_series(10))


def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print("The factorial of the given number:")
print(factorial(5))