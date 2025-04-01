#Finding the hypotenuse of a right triangle

import math

a = float(input(f"Enter side A: "))
b = float(input(f"Enter side B: "))

c = round(math.sqrt(pow(a, 2)+ pow(b, 2))) # c = sqrt(a^2+b^2)
print(f"Side C = {c}")
