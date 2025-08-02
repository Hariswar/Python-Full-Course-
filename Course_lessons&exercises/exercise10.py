# format specifiers = {value:flags} format a value based on what 
#                              flags are inserted 

# .(number)f = round to that many decimal places(fixed point)
# :(number) = allocate that many spaces 
# :03 = allocate and zero pad that many spaces 
# :< = left justify
# :> = right justify 
# :^ = center align
# :+ = use a plus sign to indicate positive values 
# := = place sign to leftmost position
# : = insert a space before positive numbers 
# :, = comma separator

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:.2f}") # output: Price 1 is $3.14
print(f"Price 2 is ${price2:10}") # output: Price 2 is $   -987.65
print(f"Price 3 is ${price3:010}") # output: Price 3 is $0000012.34
print(f"Price 1 is ${price1:>10}") # output: Price 1 is $      3.14
print(f"Price 2 is ${price2:^10}") # output: Price 2 is $  -987.65

price4 = 3000.14159

print(f"Price 4 is ${price4:+,.2f}") # output: Price 4 is $+3,000.14


