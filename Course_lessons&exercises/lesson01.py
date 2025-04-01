#This is my first program 
print('Hello world')
print("It's really good!")

# Variable = It is an container for a value (string, integer, float, boolean)
# A variable behaves as if it was the value it contains. 

#Strings 
first_name = "Hariswar"
food = "pizza"
email = "1234@gmail.com"

print(first_name)
print(f"Hello {first_name}") # f - means format #Output would be Hello Hariswar 
print(f"You like {food}")
print(f"Your email is: {email}")

#Integers - don't need to be in quotes since it's not an string. Whole Numbers!
age = 18
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#Float - decimal
price = 10.99
gpa = 4.0
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance}km")

#Boolean - True/False
#Example 1:
is_student = False 

if is_student:
  print("You are a student")
else:
  print("You are NOT a student")

#Example 2: 
for_sale = True 

if for_sale: #Since for_sale is true, we will print the first statement. If it's false, we will print the second sentence. 
  print("That item is for sale")
else:
  print("That item is NOT available")


