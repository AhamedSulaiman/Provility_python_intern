#Placeholder and modifier
cost=5
print(f"The cost of the tea is {cost} rupees")

#displaying price with decimal
print(f"The cost of the tea with two decimal is {cost:.2f}")

print(f"The cost of the tea with two decimal is {100:.2f}")

#performing operations in F-Strings

print(f"The multiplication of 2 and 3 is {2*3}")

#Performing if else inside the F-Strings

print(f"The cost of the tea is very {'Cheap' if cost<=5 else 'Expensive'}")

#Execute functions in the F-Stirng

string1="Sulaiman"
print(f"My name is {string1.upper()}")

#Create a new function and use it in a F-String
def converter(x):
    return x*80

print(f"The coverted amount of 100 USD into INR is {converter(100)}")

#Comma for seperating thousands

print(f"The amount of the car is {50000000:,}")

#multiple values

brothers=5
sisters=3
cousins=2
data="i have {} brothers {} sissters and {} cousins"
print(data.format(brothers,sisters,cousins))


bike = "I have a {bike}, it is a {model}."
print(bike.format(bike = "RX", model = "100"))