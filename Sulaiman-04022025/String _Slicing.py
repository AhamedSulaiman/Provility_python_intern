#Slicing a string
a=input("Enter a string: ")
b=a[:2]+a[4:]
print(b)

#Reversing a string and to check it is palindrome or not
print(a[::-1])
if a==a[::-1]:
    print("Its a Palindrome")
else:
    print("Not Palindrome")