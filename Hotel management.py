customers= int(input("Enter the number of customers : "))
room_charges = 0
food_cost = 0
for c in range(1, customers + 1):

    print("=======CHOOSE ROOM=======",c)
    print("1. 2star = Rs.1500/per day")
    print("2. 3star = Rs.2500/per day")
    print("3. 5star = Rs.4000/per day")
    room = int(input("Choose room 1,2,3 : "))
    days = int(input("Enter the number of days : "))

    if room == 1:
     rate = 1500
    elif room == 2:
     rate = 2500
    elif room == 3:
     rate = 4000
    else:
     print("Please select correct room from the options")
  #Food items

food_order = input("Do you want to order food ? (yes/no) :").lower()
if food_order == "yes" :
    print("=======MENU=======")
    print("1. Burger >>> Rs 50")
    print("2. Pizza >>> Rs 300")
    print("3. Pasta >>> Rs 100")
food_items =input("What would you like to order? : ").lower()
if  food_items == "burger" :
    food_cost += 50 * customers
elif food_items == "pizza" :
    food_cost += 300 * customers
elif food_items == "pasta" :
    food_cost += 100 * customers
else :
    print("Food item is not in menu...")
    
#Room charges

room_charges += (rate * days ) 
if days > 5:
    discount = (room_charges + food_cost ) *20 / 100
elif days >= 3:
    discount = (room_charges + food_cost ) *10 /100
else:
    discount = 0

#GST
subtotal = (room_charges + food_cost) - discount

gst = int(subtotal * 18//100)

final_bill = subtotal + gst

print("========FINAL BILL========")
print(f"Room charges = {room_charges}")
print(f"Food charges = {food_cost}")
print(f"Discount = {discount}")
print(f"GST = {gst}")
print(f"Final bill = {final_bill}")











    


