#while loop = execute some code WHILE some condition remains true 

name = input("Enter your name: ")

while name == "":
  print("You did not enter your name") 
  name = input("Please enter your name: ") # Prompt the user again
else:
  print(f"Hello {name}!")

#lesson 2: 

age = int(input("Enter your age: "))

while age < 0:
  print("Age can't be negative")
  age = int(input("Enter your age: "))

print(f"You are {age} years old!")



