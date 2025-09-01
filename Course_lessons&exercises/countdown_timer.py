import time 

my_time = input("Enter the time in seconds: ")

for x in range(0, my_time):
  print(x)
  time.sleep(1)

print("TIME'S UP!") 

#Example 2: 
# this will count down from the time entered to 0(so backwards)
for x in ranged(my_time, 0, -1):
  print(x)
  time.sleep(1)

print("TIME'S UP!")


