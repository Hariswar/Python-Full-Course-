# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

num = 6

# Example 1 with positive and negative numbers. 
num = 6
print("Positive" if num > 0 else "negative")

# Example 2 with even and odd numbers.
num = 8
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

# Example 3 with min and max
a = 5
b = 9

min_num = a if a < b else b
max_num = a if a > b else b

# Example 4 with age

age = 25
status = "Adult" if age >= 18 else "Child"
print(status)

# Example 5 with weather
temp = 20
weather = "HOT" if temp > 20 else "COLD"
print(weather)

# Example 6 with user role
user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)


