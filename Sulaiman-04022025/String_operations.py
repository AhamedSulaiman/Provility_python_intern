#Check the prescence of the word in the sentence

txt = "Hello,Moto   ".lower()
if "moto" not in txt:
  print("No, 'expensive' is NOT present.")
else:
  print("It is presented")

#Removing the unwanted spacing beginning and ending of the sentence

a=txt.strip()
print(a)

#Replacing one element with other
print(a.replace("h", "J"))

#Splitting the data into list if it contains the comma
print(a.split(","))

#Concatination of strings
a="I want to be "
b="a ML Engineer"
print(a+b)

#Using more quotes inside the string
txt = "We are the so-called \"Vikings\" from the north."
print(txt)