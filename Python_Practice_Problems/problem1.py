#1. User will input(3 ages). Find the oldest one. 

first_person = int(input(f"What is your age? "))
second_person = int(input(f"What is your age? "))
thirld_person = int(input(f"What is your age? "))

oldest_person = max(first_person, second_person, thirld_person) #max operator 
print(f"The oldest person is {oldest_person}")