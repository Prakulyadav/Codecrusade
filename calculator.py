num1 = int(input("Enter first number : "))
operator = input("Select = + , - , / , // , % , * , ** :  ")
num2 = int(input("Enter second number: "))
result = 0

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "/":
    if num2 == 0 :
        print("Can't divide by 0")
    else :
     result = num1 / num2
    
elif operator == "//":
    result = num1 // num2
elif operator == "%":
    result = num1 % num2
elif operator == "*":
    result = num1 * num2
elif operator == "**":
    result = num1 ** num2
else :
    print("Invalid operator")

print("Result : ", result)
