#Typecasting = the process of converting a variable from one data type to another 
# str(), int(), float(), bool()

name = "Bro Code"
age = 25
gpa = 4.0
is_student = True 

print(type(name)) # this outputs the what data type is each variable. 

#converting float to int
gpa = int(gpa)
print(gpa)

#int to float
age = float(age)
print(age)

#converts to string
age = str(age)
print(age)
print(type(age)) #shows the data type. 

#converts string to bool
#Example 1
name = bool(name)
print(name) #Output would be true 

#Example 2 
#In this case output would be false since there is no characters inside the string. 
fruit = ""
fruit = bool(fruit)
print(fruit) 

