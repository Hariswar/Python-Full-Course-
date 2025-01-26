#Exercise 8
#Example 1
name = input("Enter your name: ")

if name == "": # This is an empty string which means that this will work when user doesn't type anything. 
  print("You did not type in your name!")
else:
  print(f"Hello {name}")

  #Example 2
  for_sale = True

  if for_sale:
    print("This item is for sale") #since for_sale is true, this would be the output. 
  else:
    print("This item is NOT for sale") 

  #Example 3
  online = False 

  if online: 
    print("The user is online")
  else:
    print("The user is offline ") #since online is false, this would be the output. 

