#3. User will input (2numbers).Write a program to swap the numbers

num1 = int(input("Provide me the number: "))
num2 = int(input("Provide me the number: "))

num1 , num2 = num2, num1 
print(f"The swap values are: {num1, num2}")

