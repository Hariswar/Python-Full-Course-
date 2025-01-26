#2. Write a program that will convert celsius value to fahrenheit

celsius_value = float(input("Please give me the cesius value? "))

fahrenheit = (celsius_value * (9/5)) + 32
print(f"The fahrenheit value is {round(fahrenheit, 1)}")