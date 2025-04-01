# validate user input exercise 
# 1. username is no more than 12 characters 
# 2. username must not contain spaces 
# 3. username must not contain digits 

username = input("Enter your username: ")


if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1: # if the username contains a space, it will return a number other than -1
    print("Your username can't contain spaces")
elif not username.isalpha(): # if the username contains a number, it will return False
    print("Your username can't contain numbers")
else: 
    print(f"Welcome {username}")

  