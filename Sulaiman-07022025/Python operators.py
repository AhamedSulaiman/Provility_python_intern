#Arithmetic operator
x,y=10,5
print(x+y)

#Comparision operator
score=0
for i in range(10):
    score+=1
print(score)
# #Comparision operator

age=67
print("You are eligible to vote") if age>=18  else print("you are not eligible to vote")

#logical operator

mark=86
if mark>80 and mark<90:
    print("You got an A grade")

#Identity operator
x=[1,2,3,4,5]
y=[1,2,3,4,5]
z=x

print(x is y)
print(y is z)
print(x is z)


#Membership operator
print("Check whether the given element is in the other list")
print(x[0] in y)

#Bitwise operator

print(~7)

