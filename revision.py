'''

a = 10 * 2.0
b = True + True + True
c = 10 / 2
d = 10 // 3
e = bool(0.0001)
f = bool("")
g = int(-9.7)
h = int(True) + float(False)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))
'''


'''


print(2 + 3 * 4 ** 2 // 8 - 1)

print((2 + 3) * 4 ** 2 // (8 - 1))

print(2 ** 3 ** 2)

print(-2 ** 4)

print((-2) ** 4)
'''


'''


s1, s2, s3, s4, s5 = 78, 85, 90, 72, 88

# Wrong result
wrong = s1 + s2 + s3 + s4 + s5 / 5
print("Wrong  :", wrong)

# Correct result
correct = (s1 + s2 + s3 + s4 + s5) / 5
print("Correct:", correct)
'''


'''


n = 6789

# a) Extract last digit
print("Last digit:", n % 10)

# b) Extract last two digits
print("Last two digits:", n % 100)

# c) Round to nearest hundred
print("Nearest hundred:", ((n + 50) // 100) * 100)

# d) Check divisibility by 9
print("Divisible by 9:", n % 9 == 0)
'''


'''


print(5 == 5.0)

print(5 is 5.0)

print(type(5) == type(5.0))

print(type(1) == type(True))

print(isinstance(True, int))

print(0 == False == 0.0)
'''





'''


print(
    f"The area of a circle with radius 7 is approximately "
    f"{3.14159 * 7 ** 2:.2f}"
)
'''


'''


item     = "Notebook"
price    = 120
quantity = 5
discount = 10
tax      = 5

# Calculate subtotal
subtotal = price * quantity

# Calculate discount
discount_amount = subtotal * discount / 100

# Calculate tax after discount
tax_amount = (subtotal - discount_amount) * tax / 100

# Calculate total
total = subtotal - discount_amount + tax_amount

# Calculate savings
savings = discount_amount

print("---- Receipt ----")
print(f"Item       : {item}")
print(f"Unit Price : ₹{price}")
print(f"Quantity   : {quantity}")
print(f"Subtotal   : ₹{subtotal}")
print(f"Discount   : ₹{discount_amount}   ({discount}%)")
print(f"Tax        : ₹{tax_amount}   ({tax}%)")
print(f"Total      : ₹{total}")
print(f"Savings    : ₹{savings}")
print("------------------")
'''