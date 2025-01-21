#Exercise 2 Shopping Cart Program

item = input(f"What item would you like to buy?: ")
price = float(input(f"What is the price?: "))
quantity = int(input(f"How mnay would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")
