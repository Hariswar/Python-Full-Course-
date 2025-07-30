# indexing = accessing elements of a sequence using [] (indexing operators)
#         [start : end : step]

#lesson 1

credit_number = "1234-5678-9012-3456"

print(credit_number[0])  # Output: '1'
print(credit_number[0:4])  # Output: '1234'
print(credit_number[5:9])  # Output: '5678'
print(credit_number[5:]) # Output: '5678-9012-3456'
print(credit_number[-1])  # Output: '6'
print(credit_number[::2 ])  # Output: '135790246'

#lesson 2
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")  # Output: 'XXXX-XXXX-XXXX-3456'

credit_number = credit_number[::-1]
print(credit_number)  # Output: '6543-2109-8765-4321'