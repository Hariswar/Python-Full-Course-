#input() = A function that prompts the user to enter data 
#          Returns the entered data as a string 

name = input("What is ur name?: ") #Asks for your name
print(f"Hello {name}!")

age = input("How old are you?: ")
age = int(age) #Turns the string into an int
print(f"You are {age} years old")
