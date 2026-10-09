'''
name = "Bhavishya"
age = "19"
# print(name[0:3])
# print(name[:])
# print(name[4:1])
# x = name[0:5]
# print(x)
# print(name)
# print(name[0:100])

# print(name[0: :2])

# print(name[-7:-1])
# print(name[: : -2])
# print(name[: : -1])
# print(name[-1 : -7])
# print(name[-5:-1])

# print(f"My name is : {name} and my age is {age}")
'''

'''
age =int(input("Enter your age : "))

if age >= 18 :
        print("Eligible") 
else: print("Not eligible")

'''

'''
eng = int(input("Enter your english marks / 25 : "))
maths = int(input("Enter your maths marks / 25 : "))
physics = int(input("Enter your physics marks /25: "))
chemistry = int(input("Enter your chemistry marks / 25: "))

total_marks = eng + maths + physics + chemistry

if total_marks >= 90 :
        print("Grade A")
elif total_marks >= 60 :
        print("Grade B")
elif total_marks >= 30 :
        print("Grade C")
else :
        print("Fail")

'''

'''
num = int(input("Enter a number : "))
if num % 3 == 0 :
        print(f"{num} is divisible by three")
else :
         print(f"{num} Not divisible by 3")

         '''

'''marks = int(input("Enter your marks : "))
if marks >= 30 :
        if marks >= 90:
                print("Grade A")
        elif marks >= 50 :
                print("Grade B")
     
        else :
                print("Grade C")
else:
        print("FAIL")
        '''

'''
age =int(input("Enter your age : "))
driving_licence = (input("Do you have a driving license? : ").lower())
is_drive = driving_licence == "yes"

if age >= 18 :

    if is_drive == True:
        print("Your can drive")
    else : 
        print("Apply for a driving license")
else: 
    print("Not eligible")
    '''

num =(int(input("Enter a number : ")))

if num > 0 :
    print(f"{num} is positive.")

elif num < 0 :
    print(f"{num} is negative")

else :
    print("Zero")

  


