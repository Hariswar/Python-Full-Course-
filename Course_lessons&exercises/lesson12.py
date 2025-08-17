#for loops = execute a block of code a fixed number of times. 
#            You can iterate over a range, string, sequence, etc. 

# Example 1: 
for x in range(1, 11): # 1 - 10
  print(x) 
  # Output would be 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# Example 2:
for x in reversed(range(1,11)):
  print(x)
print("Happy new year!")
# Output would be 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 Happy new year!

# Example 3:
for x in range(1, 11, 2): # 1 - 10, increment by 2
  print(x)
# Output would be 1, 3, 5, 7, 9

#Example 4:
credit_card = "1234-5678-9012-3456"

for x in credit_card:
  print(x)
# Output would be 1, 2, 3, 4, -, 5, 6, 7, 8, -, 9, 0, 1, 2, -, 3, 4, 5, 6

