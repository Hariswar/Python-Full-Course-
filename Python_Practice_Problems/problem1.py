#1. User will input(3 ages). Find the oldest one. 
# There is two ways to this, one is using the max operator and the other is using the if-elif statement.

# Using the max operator

first_person = int(input(f"What is your age? "))
second_person = int(input(f"What is your age? "))
third_person = int(input(f"What is your age? "))

oldest_person = max(first_person, second_person, third_person) #max operator 
print(f"The oldest person among the three people is {oldest_person}")

# Using the if-elif statement
if first_person > second_person and first_person > third_person:
    print(f"The oldest person is {first_person}")
elif second_person > first_person and second_person > third_person:
    print(f"The oldest person is {second_person}")
elif third_person > first_person and third_person > second_person:
    print(f"The oldest person is {third_person}")
elif first_person == second_person and first_person > third_person:
    print(f"Two people have the same age and they are the oldest: {first_person} and {second_person}")
elif first_person == third_person and first_person > second_person:
    print(f"Two people have the same age and they are the oldest {first_person} and {third_person}")
elif second_person == third_person and second_person > first_person:
    print(f"Two people have the same age and they are the oldest {second_person} and {third_person}")
elif first_person == second_person == third_person:
    print(f"All three people have the same age: {first_person}")
