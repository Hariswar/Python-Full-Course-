# Math Functions 

# Basic Math Functions 

x = 3.14
y = 4
z = 5

result = round(x)
result = abs(y)
result = pow(4,3) # this means 4 to the power of three which is 64. 
result = max(x,y,z) #finds the maximum digit between x,y,z. 
result = min(x,y,z) #finds the min digit between x,y,z. 

# For advanced math features you have to import math. 

import math

print(math.pi) #displays the digits for pi. 
print(math.e) #displays the digits for pi. 

#displays the square root of an number
x = 9
result = math.sqrt(x)
print(result)

#displays the round up value of an floating point number. 
y = 9.3
value = math.ceil(y)
print(value) #output is 10

#displays the round down value of an floating point number. 
y = 9.3
num = math.floor(y)
print(num) #output is 9



