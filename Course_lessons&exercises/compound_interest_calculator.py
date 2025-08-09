# Python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
  principle = float(input("Enter the principal amount: "))
  if principle <= 0:
    print("Principle can't be less than or equal to zero")

while rate <= 0:
  rate = float(input("Enter the rate of interest: "))
  if rate <= 0:
    print("Rate of interest can't be less than or equal to zero")

while time <= 0:
  time = int(input("Enter the time in years: "))
  if time <= 0:
    print("Time can't be less than or equal to zero")
  
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")

# Different way to write this code: 

principle1 = 0
rate1 = 0
time1 = 0

while True: 
  principle1 = float(input("Enter the principal amount: "))
  if principle1 > 0:
    print("Principle can't be less than zero")
  else:
    break 

while True:
  rate1 = float(input("Enter the rate of interest: "))
  if rate1 > 0:
    print("Rate of interest can't be less than zero")
  else:
    break

while True:
  time1 = int(input("Enter the time in years: "))
  if time1 > 0:
    print("Time can't be less than zero")
  else:
    break

total1 = principle1 * pow((1 + rate1 / 100), time1)
print(f"Balance after {time1} year/s: ${total1:.2f}")
