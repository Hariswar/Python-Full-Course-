# usefull string methods 

print(help(str)) # returns all the methods that can be used with strings.

# Got a feww examples of string methods below.
name = input("Enter your name: ")
phone_number = input("Enter your phone number #: ")

result = len(name) # returns the length of the string that include spaces too. 
name.find("a") # returns the number that the letter "a" is found in the string. it starts with zero. 
name.find("b") # returns -1 if the letter is not found in the string.
name.capitalize() # returns the first letter of the string capitalized.
name.upper() # returns the entire string in uppercase.
name.lower() # returns the entire string in lowercase.
name.isdigit() # returns True if the string is a number. The entire string must be a number. if it's a mix of letters and numbers, it will return False. It would also return False if the string is fully letters.
name.isalpha() # returns True if the string is fully letters. It would return False if the string is a mix of letters and numbers or if it's fully numbers.
print(result)

result = phone_number.count("-") # returns the number of times the "-" is found in the string.
phone_number.replace("-", " ") # replaces the "-" with an space.
print(phone_number)



