#input() = A function that prompts the user to enter data 
#          Returns the entered data as a string 

name = input("What is ur name?: ") #Asks for your name
print(f"Hello {name}!")

#Example 1

age = input("How old are you?: ")
age = int(age) #Turns the string into an int
age = age + 1
print(f"You are {age} years old")

#OR 
ages = int(input("How old are you?: "))
ages = ages + 1
print(f"You are {ages} years old")

